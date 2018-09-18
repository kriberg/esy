import logging
from types import MethodType
from .client import ESIClient, ESICallableOperation

log = logging.getLogger(__name__)


class Entity(object):
    def __init__(self, entity_type, entity_key, entity_id, resource_key, client,
                 _token=None) -> None:
        super().__init__()
        self._entity_type = entity_type
        self._entity_kwarg = {entity_key: entity_id,
                              '_token': _token}
        self._entity_id = entity_id
        self._token = _token
        self._client = client
        self._resource_context = {}
        self._resource_key = resource_key
        self._public_attributes = []
        self._register_resources(self._entity_type)
        self._augment_operations()

    def __str__(self):
        return f'{self._entity_type} {self._entity_id}'

    @property
    def id(self):
        return self._entity_id

    def set_token(self, token):
        '''
        Sets the token used for calling ESI operations.

        :param str token: ESI authorization token
        :return:
        '''
        self._token = token
        self._entity_kwarg['_token'] = token

    def _register_resources(self, entity_type):
        # All resources should be ESICallableOperation wrappers
        # We start with mapping the base resource's response specification
        # as top-level attributes to our resource context
        if entity_type is self._entity_type:
            base_resource = getattr(entity_type, self._resource_key)
            self._resource_context.update(self._map_resource(base_resource))

    def _map_operation(self, context_name, operation):
        def wrapper(self, *args, **kwargs):
            kwarg = {**self._entity_kwarg, **kwargs}
            return operation(*args, **kwarg)

        bound_method = MethodType(wrapper, self)
        bound_method.__func__.__name__ = context_name
        bound_method.__func__.__doc__ = operation.op_spec.get('summary')
        bound_method.__func__.__annotations__ = {'parameters': []}

        for parameter in _OPERATION_PARAMETER_MAPPING.keys():
            if parameter in context_name:
                bound_method.__func__.__annotations__['parameters'].append(
                    parameter)
                context_name = context_name.replace(
                    parameter, _OPERATION_PARAMETER_MAPPING[parameter])

        setattr(self, context_name, bound_method)

    def _map_resource(self, operation):
        context = {}
        # Strap on your helmet, we're drilling deep into bravado
        schema = operation.op_spec['responses']['200']['schema']

        # Some responses are objects, while others are arrays. For objects, we
        # will map their properties, as per their schema, as attributes. While
        # for arrays, we will map it directly
        for prop, _ in schema['properties'].items():
            assert prop not in context
            context[prop] = operation
            if prop in _PROPERTY_ATTRIBUTE_MAPPING:
                self._public_attributes.append(
                    _PROPERTY_ATTRIBUTE_MAPPING[prop])
            else:
                self._public_attributes.append(prop)
        return context

    def _augment_operations(self):
        for resource_name in dir(self._client):
            resource = getattr(self._client, resource_name)
            for service_name in dir(resource):
                if service_name == self._resource_key:
                    continue
                if service_name.startswith(self._resource_key):
                    service = getattr(resource, service_name)
                    context_name = service_name.replace(self._resource_key,
                                                        'get')
                    assert type(service) is ESICallableOperation
                    self._map_operation(context_name, service)

    def __getattr__(self, attribute_name):
        if attribute_name in _ATTRIBUTE_PROPERTY_MAPPING:
            pname = _ATTRIBUTE_PROPERTY_MAPPING[attribute_name]
        else:
            pname = attribute_name
        try:
            resource = self._resource_context[pname]
        except KeyError:
            raise AttributeError

        # Any wrapped operations should not hit __getattr__, but be called
        # directly.
        assert type(resource) is ESICallableOperation

        if resource.require_authorization:
            kwarg = {**self._entity_kwarg, '_token': self._token}
        else:
            kwarg = self._entity_kwarg

        result = resource(**kwarg).get(pname)
        if attribute_name in _ATTRIBUTE_ENTITY_MAPPING:
            klass = _ATTRIBUTE_ENTITY_MAPPING[attribute_name]
            return klass(result, _client=self._client, _token=self._token)
        return result

    def __eq__(self, other):
        return self._entity_type.resource.name == \
               other._entity_type.resource.name and \
               self._entity_id == other._entity_id

    def __dir__(self):
        entries = list(super().__dir__())
        entries.extend(self._public_attributes)
        return entries

    @classmethod
    def from_names(cls, *names, _client=None, _token=None):
        '''
        Initialize a set of entities from a list of names

        :param list *names:
        :param ESIClient _client:
        :param str _token:
        :return:
        :rtype: dict
        '''
        client = _client or ESIClient.get_client()
        resolved_ids = client.Universe.post_universe_ids(names=names)
        entities = {}
        for entity_type, results in resolved_ids.items():
            entity_class = None
            if entity_type == 'characters':
                entity_class = Character
            elif entity_type == 'corporations':
                entity_class = Corporation
            elif entity_type == 'alliances':
                entity_class = Alliance

            if results:
                for result in results:
                    entities[result['name']] = entity_class(result['id'],
                                                            _client=client,
                                                            _token=_token)
        return entities

    @classmethod
    def from_name(cls, name, _client=None, _token=None):
        '''
        Initialize an entity from a name

        :param str name:
        :param ESIClient _client:
        :param str _token:
        :return:
        '''
        return cls.from_names(name, _client=_client, _token=_token).get(name)


class Character(Entity):
    _RESOURCE_KEY = 'get_characters_character_id'

    def __init__(self, character_id, _client=None, _token=None) -> None:
        client = _client or ESIClient.get_client()
        super().__init__(client.Character, 'character_id', character_id,
                         Character._RESOURCE_KEY, client, _token)


class Corporation(Entity):
    _RESOURCE_KEY = 'get_corporations_corporation_id'

    def __init__(self, corporation_id, _client=None, _token=None) -> None:
        client = _client or ESIClient.get_client()
        super().__init__(client.Corporation, 'corporation_id', corporation_id,
                         Corporation._RESOURCE_KEY, client, _token)


class Alliance(Entity):
    _RESOURCE_KEY = 'get_alliances_alliance_id'

    def __init__(self, alliance_id, _client=None, _token=None) -> None:
        client = _client or ESIClient.get_client()
        super().__init__(client.Alliance, 'alliance_id', alliance_id,
                         Alliance._RESOURCE_KEY, client, _token)


_ATTRIBUTE_ENTITY_MAPPING = {
    'character': Character,
    'corporation': Corporation,
    'alliance': Alliance,
    'creator_corporation': Corporation,
}

_ATTRIBUTE_PROPERTY_MAPPING = {
    'character': 'character_id',
    'corporation': 'corporation_id',
    'alliance': 'alliance_id',
    'creator_corporation': 'creator_corporation_id'
}

_OPERATION_PARAMETER_MAPPING = {
    'planet_id': 'planet',
    'mail_id': 'mail',
    'event_id': 'event',
    'contract_id': 'contract',
    'starbase_id': 'starbase',
}

_PROPERTY_ATTRIBUTE_MAPPING = {v: k for k, v in
                               _ATTRIBUTE_PROPERTY_MAPPING.items()}
