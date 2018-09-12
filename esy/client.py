import requests
import json
import logging
import pytz
from datetime import datetime
from email.utils import parsedate
from bravado.config import RequestConfig
from bravado.client import SwaggerClient, ResourceDecorator, \
    CallableOperation, warn_for_deprecated_op, construct_request
from bravado.http_future import HttpFuture
from bravado.requests_client import RequestsClient, RequestsFutureAdapter, \
    RequestsResponseAdapter
from bravado_core.spec import Spec
from bravado.exception import HTTPInternalServerError, HTTPNotFound, \
    HTTPBadRequest, HTTPForbidden
from .exceptions import ESIError, ESINotFound, ESIForbidden, \
    ESIAuthorizationError
from .constants import ESI_ENDPOINT, ESI_DATASOURCE, ESI_SWAGGER_CACHE_TIMER, \
    ESY_USER_AGENT


log = logging.getLogger(__name__)


class ESICallableOperation(CallableOperation):
    """
    Wraps bravado's CallableOpeartion to handle pagination
    """

    def __init__(self, operation):
        self.operation = operation
        self.require_authorization = any(map(lambda spec: 'evesso' in spec,
                                             self.operation.security_specs))
        super(ESICallableOperation, self).__init__(operation)
        self.paginated = 'page' in operation.params

    def __call__(self, _token=None, **op_kwargs):
        """Invoke the actual HTTP request and return a future.

        :rtype: :class:`bravado.http_future.HTTPFuture`
        """
        warn_for_deprecated_op(self.operation)

        # Apply request_options defaults
        request_options = op_kwargs.pop('_request_options', {})
        request_config = RequestConfig(request_options,
                                       also_return_response_default=True)

        request_params = construct_request(
            self.operation, request_options, **op_kwargs)

        # config = self.operation.swagger_spec.config
        http_client = self.operation.swagger_spec.http_client

        # Per-request config overrides client wide config
        # also_return_response = request_options.get(
        #     'also_return_response',
        #     config['also_return_response'])

        # Check if we need an authorization token and if so set it up
        if self.require_authorization and _token is None:
            raise ESIAuthorizationError('Missing required authorization token')

        return http_client.request(
            request_params,
            operation=self.operation,
            request_config=request_config,
            authorization_token=_token)


class ESIPageGenerator(object):
    """
    Generator for ESI API calls.
    """
    def __init__(self, requests_future, requestsresponse_adapter, operation,
                 response_callbacks, request_config, cache=None):
        self.requests_future = requests_future
        self.requestsresponse_adapter = requestsresponse_adapter
        self.operation = operation
        self.response_callbacks = response_callbacks
        self.request_config = request_config
        self.page = 1
        self.num_pages = 1
        self.stop = False
        self.cache = cache
        if self.cache is not None:
            assert callable(getattr(self.cache, 'get', None))
            assert callable(getattr(self.cache, 'set', None))
            assert callable(getattr(self.cache, '__contains__', None))

    def __iter__(self):
        return self

    def _get_cache_key(self):
        return hash((
            self.requests_future.request.url,
            str(self.requests_future.request.params),
            str(self.requests_future.request.auth),
            str(self.requests_future.request.headers),
            str(self.requests_future.request.method),
            self.page
        ))

    def _send(self):
        return HttpFuture(self.requests_future,
                          self.requestsresponse_adapter,
                          operation=self.operation,
                          request_config=self.request_config).result()

    def result(self):
        if self.cache is not None:
            key = self._get_cache_key()
            if key in self.cache:
                data, num_pages = self.cache.get(key)
                self.num_pages = num_pages
            else:
                data, response = self._send()
                self.num_pages = int(response.headers.get('x-pages', '1'))
                expire_header = response.headers.get('expires')
                if expire_header is not None:
                    expires = datetime(
                        *parsedate(response.headers.get('expires'))[:7],
                        pytz.UTC)
                    self.cache.set(key, (data, self.num_pages), expires)
        else:
            try:
                data, response = self._send()
            except HTTPForbidden:
                raise ESIForbidden('Access denied')
            self.num_pages = int(response.headers.get('x-pages', '1'))

        return data

    def get(self):
        try:
            return self.result()
        except (HTTPInternalServerError,
                HTTPBadRequest) as ex:  # pragma: no cover
            raise ESIError(str(ex))
        except HTTPNotFound as ex:  # pragma: no cover
            try:
                error_msg = json.loads(ex.response.text)
                raise ESINotFound(error_msg.get('error', 'Not found'))
            except Exception as ex:
                raise ESINotFound(str(ex))
        except HTTPForbidden:  # pragma: no cover
            raise ESIForbidden('Access denied')

    def __next__(self):
        if self.stop:
            self.requests_future.session.close()
            raise StopIteration
        else:
            self.requests_future.request.params['page'] = self.page
            swagger_result = self.result()
            self.page += 1
            if self.page > self.num_pages:
                self.stop = True
            return swagger_result


class ESIRequestsClient(RequestsClient):
    """
    Extends the bravado RequestsClient to handle pagination, user agent and
    per-request authorizations.
    """
    def __init__(self, user_agent, cache=None):
        super().__init__()
        self.user_agent = user_agent
        self.cache = cache

    def request(self, request_params, operation=None, response_callbacks=None,
                request_config=None, authorization_token=None):
        sanitized_params, misc_options = self.separate_params(request_params)
        session = requests.Session()
        if authorization_token:
            session.headers.update({
                'Authorization': 'Bearer {}'.format(authorization_token)
            })
        session.headers.update({
            'User-Agent': self.user_agent
        })

        requests_future = RequestsFutureAdapter(
            session,
            self.authenticated_request(sanitized_params),
            misc_options,
        )

        if operation is not None and 'page' in operation.params:
            return ESIPageGenerator(requests_future,
                                    RequestsResponseAdapter,
                                    operation,
                                    response_callbacks,
                                    request_config=request_config,
                                    cache=self.cache)
        else:
            data = ESIPageGenerator(requests_future,
                                    RequestsResponseAdapter,
                                    operation,
                                    response_callbacks,
                                    request_config=request_config,
                                    cache=self.cache).get()
            session.close()
            return data


class ESIClient(SwaggerClient):
    """
    Swagger client interface adapted to use with the ESI.
    """

    def __init__(self, swagger_spec, esi_endpoint, user_agent, use_models,
                 cache):
        """
        Internal constructor for ESIClient. Use get_client instead of
        instancing ESIClient directly.

        :param swagger_spec:
        :param esi_endpoint:
        :param user_agent:
        :param use_models:
        :param cache:
        """
        self.http_client = ESIRequestsClient(user_agent, cache=cache)
        swagger_spec = Spec.from_dict(swagger_spec,
                                      esi_endpoint,
                                      self.http_client,
                                      config={
                                          'use_models': use_models
                                      })
        super(ESIClient, self).__init__(swagger_spec)

    @staticmethod
    def _generate_esi_endpoint(endpoint, datasource):
        return '{}?datasource={}'.format(endpoint, datasource)

    @staticmethod
    def get_client(user_agent=ESY_USER_AGENT, use_models=False, spec=None,
                   endpoint=ESI_ENDPOINT, datasource=ESI_DATASOURCE,
                   cache=None):
        """
        Generates a client interface for ESI.

        :param user_agent:
        :type user_agent: str
        :param use_models:
        :param spec:
        :param endpoint:
        :type endpoint: str
        :param datasource:
        :type datasource: str
        :param cache: A class which implements the cache interface
        :return: An initalized client
        :rtype: ESIClient
        """
        target = ESIClient._generate_esi_endpoint(endpoint, datasource)
        if spec is None:
            spec = ESIClient.get_swagger_spec(endpoint=endpoint,
                                              datasource=datasource)
        return ESIClient(spec, target, user_agent, use_models, cache)

    @staticmethod
    def get_swagger_spec(endpoint=ESI_ENDPOINT, datasource=ESI_DATASOURCE,
                         cache=None):
        """
        Downloads and parses the swagger specification from the ESI endpoint.

        :param endpoint: URL to the ESI endpoint. Defaults to latest.
        :type endpoint: str
        :param datasource: ESI datasource to use. Defaults to Tranquility.
        :type datasource: str
        :param cache: Optional cache
        :return: Swagger specification
        :rtype: dict
        """
        endpoint = ESIClient._generate_esi_endpoint(endpoint, datasource)
        key = hash((endpoint, 'spec'))
        if cache is not None and key in cache:
            swagger_data = cache.get(key)
        else:
            try:
                start = datetime.now()
                resp = requests.get(endpoint)
                resp.raise_for_status()
                swagger_data = resp.text
                log.debug('Swagger spec downloaded in {} seconds'.format(
                    datetime.now() - start
                ))
            except Exception as ex:
                error = 'Could not connect to ESI: {}'.format(ex)
                log.error(error)
                raise ESIError(error)

        if cache is not None and key not in cache:
            cache.set(key, swagger_data, ESI_SWAGGER_CACHE_TIMER)

        try:
            spec = json.loads(swagger_data)
            return spec
        except Exception as ex:  # pragma: no cover
            error = 'Could not parse ESI swagger specification: {}'.format(ex)
            log.error(error)
            raise ESIError(error)

    @property
    def cache(self):
        return self.http_client.cache

    @cache.setter
    def cache(self, cache):
        self.http_client.cache = cache

    def __getattr__(self, item):
        resource = self.swagger_spec.resources.get(item)
        if not resource:
            raise AttributeError('Resource {0} not found. Available '
                                 'resources: {1}'.format(item,
                                                         ', '.join(dir(self))))

        # Wrap bravado-core's Resource and Operation objects in order to
        # execute a service call via the http_client.
        return ESIResourceDecorator(resource)


class ESIResourceDecorator(ResourceDecorator):
    """
    Extends ResourceDecorator to wrap operations with ESICallableOperation
    """

    def __getattr__(self, name):
        """
        :rtype: :class:`CallableOperation`
        """
        return ESICallableOperation(getattr(self.resource, name))

    def __eq__(self, other):
        """
        :param other: instance to compare to
        :type other: ESIResourceDecorator
        :return: equality of instances
        :rtype: bool
        """
        return self.resource.name == other.resource.name

    def __str__(self):
        return self.resource.name
