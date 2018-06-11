import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from .constants import ESI_ACCESS_TOKEN_ENDPOINT, ESI_TOKEN_VERIFY_ENDPOINT, \
    ESI_REVOKE_TOKEN_ENDPOINT


class ESIAuthenticator(object):
    """
    Handles ESI token authentication and verification process.
    """

    def __init__(self, access_token_endpoint=ESI_ACCESS_TOKEN_ENDPOINT,
                 token_verify_endpoint=ESI_TOKEN_VERIFY_ENDPOINT,
                 revoke_token_endpoint=ESI_REVOKE_TOKEN_ENDPOINT):
        """
        Creates a handler for ESI authentication and verification.

        :param access_token_endpoint: URL to the ESI access token endpoint.
        :type access_token_endpoint: str
        :param token_verify_endpoint: URL to the ESI token verify endpoint.
        :type token_verify_endpoint: str
        :param revoke_token_endpoint: URL to the ESI revoke token endpoint.
        :type revoke_token_endpoint: str
        """
        self.access_token_endpoint = access_token_endpoint
        self.token_verify_endpoint = token_verify_endpoint
        self.revoke_token_endpoint = revoke_token_endpoint

    def verify_authorization_code(self, authorization_code, client_id, secret):
        """
        Trades an authorization code for a refresh and an access tokens from ESI

        :param authorization_code: The authorization code returned from ESI
        :type authorization_code: str
        :param client_id: The ESI ClientID
        :type client_id: str
        :param secret: The ESI Secret key
        :type secret: str
        :return: (refresh_token, access_token)
        :rtype: tuple
        """
        session = OAuth2Session(client_id)
        auth = HTTPBasicAuth(client_id,
                             secret)
        resp = session.fetch_token(self.access_token_endpoint,
                                   code=authorization_code,
                                   auth=auth)
        return resp.get('refresh_token'), resp.get('access_token')

    def verify_access_token(self, access_token):
        """
        Verifies the refresh token with the ESI and retrieves character
        information.

        :param access_token: ESI access token
        :type access_token: str
        :return: dict with CharacterID, CharacterName and CharacterOwnerHash
        :rtype: dict
        """
        with requests.Session() as session:
            session.headers.update({
                'Authorization': 'Bearer {}'.format(access_token)
            })
            resp = session.get(self.token_verify_endpoint)
            resp.raise_for_status()
            return resp.json()

    def get_access_token(self, refresh_token, client_id, secret,
                         session=None, auth=None):
        """
        Get a new access token using a refresh token

        :param refresh_token: The refresh token
        :type refresh_token: str
        :param client_id: The ESI ClientID
        :type client_id: str
        :param secret: The ESI Secret key
        :type secret: str
        :param session: Existing session for reuse
        :type session: OAuth2Session
        :param auth: Existing authentication handler for reuse
        :type auth: HTTPBasicAuth
        :return: New access token
        :rtype: str
        """
        if session is None:
            session = OAuth2Session(client_id)
        if auth is None:
            auth = HTTPBasicAuth(client_id,
                                 secret)
        resp = session.refresh_token(self.access_token_endpoint,
                                     refresh_token=refresh_token,
                                     auth=auth)
        return resp.get('access_token')

    def revoke_token(self, token, client_id, secret,
                     token_type='refresh_token', session=None, auth=None):
        """
        Revoke refresh or access tokens.

        :param token: The token to revoke
        :type token: str
        :param client_id: The ESI ClientID
        :type client_id: str
        :param secret: The ESI Secret key
        :type secret: str
        :param session: Existing session for reuse
        :type session: OAuth2Session
        :param auth: Existing authentication handler for reuse
        :type auth: HTTPBasicAuth
        :return: Token revocation status
        :rtype: bool
        """
        if session is None:
            session = OAuth2Session(client_id)
        if auth is None:
            auth = HTTPBasicAuth(client_id,
                                 secret)
        resp = session.post(self.revoke_token_endpoint,
                            data={
                                'token_type': token_type,
                                'token': token
                            },
                            auth=auth)
        return resp.status_code == 200
