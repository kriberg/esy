from .client import ESIClient, ESICallableOperation


class Entity(object):
    def __init__(self, entity_type, entity_key, entity_id, resource_key, client,
                 _token=None) -> None:
        super().__init__()
        self.entity_type = entity_type
        self.entity_kwarg = {entity_key: entity_id}
        self.entity_id = entity_id
        self._token = _token
        self.client = client
        self.resource_context = {}
        self.resource_key = resource_key
        self._public_attributes = []
        self._register_resources()

    @property
    def id(self):
        return self.entity_id

    def _register_resources(self):
        # All resources should be ESICallableOperation wrappers
        # We start with mapping the base resource's response specification
        # as top-level attributes to our resource context
        base_resource = getattr(self.entity_type, self.resource_key)
        self.resource_context.update(self._map_resource(base_resource))

        # For the remaining operations, we setup sub-contexts matching
        # their resource names
        for resource_name in dir(self.entity_type):
            if resource_name == self.resource_key:
                continue

            if resource_name.startswith(self.resource_key):
                operation = getattr(self.entity_type, resource_name)
                context_name = 'get{}'.format(
                    resource_name.replace(self.resource_key, ''))
                context = self._map_resource(operation)
                self.resource_context[context_name] = context
                self._public_attributes.append(context_name)

    def _map_resource(self, operation):
        context = {}
        # Strap on your helmet, we're drilling deep into bravado
        schema = operation.op_spec['responses']['200']['schema']

        # Some responses are objects, while others are arrays. For objects, we
        # will map their properties, as per their schema, as attributes. While
        # for arrays, we will map it directly
        if schema['type'] == 'object':
            for prop, _ in schema['properties'].items():
                assert prop not in context
                context[prop] = operation
                if prop in _PROPERTY_ATTRIBUTE_MAPPING:
                    self._public_attributes.append(
                        _PROPERTY_ATTRIBUTE_MAPPING[prop])
                else:
                    self._public_attributes.append(prop)
            return context
        elif schema['type'] == 'array':
            return operation

        return context

    def __getattr__(self, attribute_name):
        if attribute_name in _ATTRIBUTE_PROPERTY_MAPPING:
            pname = _ATTRIBUTE_PROPERTY_MAPPING[attribute_name]
        else:
            pname = attribute_name
        try:
            resource = self.resource_context[pname]
        except KeyError:
            raise AttributeError
        if type(resource) is ESICallableOperation:
            if resource.require_authorization:
                kwarg = {**self.entity_kwarg, '_token': self._token}
            else:
                kwarg = self.entity_kwarg

            if attribute_name.startswith('get_'):
                return lambda: resource(**kwarg)
            else:
                result = resource(**kwarg).get(pname)
                if attribute_name in _ATTRIBUTE_ENTITY_MAPPING:
                    klass = _ATTRIBUTE_ENTITY_MAPPING[attribute_name]
                    return klass(result, _client=self.client,
                                 _token=self._token)
            return result
        else:
            raise TypeError('Attribute {} is not ESICallableOperation'.format(
                attribute_name))

    def __eq__(self, other):
        return self.entity_type.resource.name == \
               other.entity_type.resource.name and \
               self.entity_id == other.entity_id

    def __dir__(self):
        return self._public_attributes

    @classmethod
    def from_names(cls, names, _client=None, _token=None):
        client = _client or ESIClient.get_client()
        resolved_ids = client.Universe.post_universe_ids(names=names)
        entities = {}
        for entity_type, results in resolved_ids.items():
            entity_klass = None
            if entity_type == 'characters':
                entity_klass = Character
            elif entity_type == 'corporations':
                entity_klass = Corporation
            elif entity_type == 'alliances':
                entity_klass = Alliance

            if results:
                for result in results:
                    entities[result['name']] = entity_klass(result['id'],
                                                            _client=client,
                                                            _token=_token)
        return entities

    @classmethod
    def from_name(cls, name, _client=None, _token=None):
        return cls.from_names([name], _client=_client, _token=_token).get(name)


class Character(Entity):
    RESOURCE_KEY = 'get_characters_character_id'

    def __init__(self, character_id, _client=None, _token=None) -> None:
        client = _client or ESIClient.get_client()
        super().__init__(client.Character, 'character_id', character_id,
                         Character.RESOURCE_KEY, client, _token)


class Corporation(Entity):
    RESOURCE_KEY = 'get_corporations_corporation_id'

    def __init__(self, corporation_id, _client=None, _token=None) -> None:
        client = _client or ESIClient.get_client()
        super().__init__(client.Corporation, 'corporation_id', corporation_id,
                         Corporation.RESOURCE_KEY, client, _token)


class Alliance(Entity):
    RESOURCE_KEY = 'get_alliances_alliance_id'

    def __init__(self, alliance_id, _client=None, _token=None) -> None:
        client = _client or ESIClient.get_client()
        super().__init__(client.Alliance, 'alliance_id', alliance_id,
                         Alliance.RESOURCE_KEY, client, _token)


_ATTRIBUTE_ENTITY_MAPPING = {
    'character': Character,
    'corporation': Corporation,
    'alliance': Alliance
}

_ATTRIBUTE_PROPERTY_MAPPING = {
    'character': 'character_id',
    'corporation': 'corporation_id',
    'alliance': 'alliance_id'
}

_PROPERTY_ATTRIBUTE_MAPPING = {v: k for k, v in
                               _ATTRIBUTE_PROPERTY_MAPPING.items()}
