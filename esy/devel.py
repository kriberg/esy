from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import threading
from requests_html import HTMLSession
from requests import Request
import random
import string
import getpass
from esy.auth import ESIAuthenticator
from esy.constants import ESI_AUTHORIZE_ENDPOINT

CLIENT_ID = os.getenv('ESY_CLIENT_ID')
SECRET_KEY = os.getenv('ESY_SECRET_KEY')
CALLBACK_URL = os.getenv('ESY_CALLBACK_URL', 'http://localhost:8000')
SERVER_ADDRESS = os.getenv('ESY_SERVER_ADDRESS', 'localhost')
SERVER_PORT = os.getenv('ESY_SERVER_PORT', '8000')
SCOPES = os.getenv('ESY_SCOPES')
SESSION = {}


class AuthenticationHandler(BaseHTTPRequestHandler):
    """
    HTTP Request handler that pilfers the state and authorization code from an
    incoming request.
    """
    DEVSERVER_HTML = bytes('<!DOCTYPE html>'
                           '<html>'
                           '<body>'
                           '<p>Authentication complete, you can close this '
                           'window now.</p>'
                           '</body>'
                           '</html>', encoding='utf-8')

    def do_GET(self):
        # First split for the last /, then strip '?', then split by '&'
        params = self.path.split('/')[-1][1:].split('&')
        for param in params:
            key, value = param.split('=')
            SESSION[key] = value
        self.send_response(200)
        self.end_headers()
        self.request.send(self.DEVSERVER_HTML)
        self.request.close()


class DevServer(HTTPServer, threading.Thread):
    """
    Tiny HTTP Server used to listen for incoming redirects from ESI, so we can
    snatch the authorization code.
    """

    def __init__(self, server_address):
        HTTPServer.__init__(self, server_address, AuthenticationHandler, True)
        threading.Thread.__init__(self)

    def run(self):
        self.handle_request()


def get_authorization_code(cli_login=False, server_address=SERVER_ADDRESS,
                           server_port=SERVER_PORT, client_id=CLIENT_ID,
                           callback_url=CALLBACK_URL, scopes=SCOPES,
                           character_id=None, username=None, password=None):
    """
    Starts an SSO session with ESI and retrieves the authorization code.
    Optionally prompts for username and password input, and character selection.

    :param cli_login: Start CLI-based authentication or just print the SSO URL.
    :type cli_login: bool
    :param server_address: The address :class:`DevServer` is binding to.
    :type server_address: str
    :param server_port: The port :class:`DevServer` is listening on.
    :type server_port: str or int
    :param client_id: The ESI ClientID
    :type client_id: str
    :param callback_url: The ESI CallbackURL
    :type callback_url: str
    :param scopes: The selected ESI scopes, as space-delimited string.
    :type scopes: str
    :param character_id: Pre-selected CharacterId to authorize
    :type character_id: str or int
    :param username: EVE Online SSO username
    :type username: str
    :param password: EVE Online SSO password
    :type password: str
    :return: authorization code
    :rtype: str
    """

    state = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                   k=16))
    dev_server = DevServer((server_address, int(server_port)))
    dev_server.start()
    if cli_login:
        _do_cli_login(callback_url, client_id, scopes, state, username,
                      password, character_id)
    else:
        request = Request('GET', ESI_AUTHORIZE_ENDPOINT, params={
            'response_type': 'code',
            'redirect_uri': callback_url,
            'client_id': client_id,
            'scope': scopes,
            'state': state
        }).prepare()
        print('Please complete the EVE SSO authentication: {}'.format(
            request.url))

    dev_server.join()
    if SESSION['state'] != state:
        print('State "{}" does not match our original state "{}"'.format(
            SESSION['state'],
            state))
        return None

    return SESSION['code']


def _do_cli_login(callback_url, client_id, scopes, state, username=None,
                  password=None, character_id=None):
    """
    My Little Browser.
    """
    session = HTMLSession()
    response = session.get(ESI_AUTHORIZE_ENDPOINT, params={
        'response_type': 'code',
        'redirect_uri': callback_url,
        'client_id': client_id,
        'scope': scopes,
        'state': state
    })
    response.raise_for_status()
    post_url = '/'.join(ESI_AUTHORIZE_ENDPOINT.split('/')[:3] +
                        [response.html.find('form',
                                            first=True).attrs.get('action')])
    if not all((username, password)):
        print('Logging in to EVE Online')
    if not username:
        username = input('Username: ')
    if not password:
        password = getpass.getpass('Password: ')
    response = response.session.post(post_url,
                                     data={'UserName': username,
                                           'Password': password})
    response.raise_for_status()
    # Fetch the input values from the response and put them into the data we
    # will send back. Most of these are identical, but never know what funk
    # will ensue.
    post_data = {}
    for input_name in ('ClientIdentifier', 'RedirectUri', 'State', 'Scope',
                       'ResponseType', '__RequestVerificationToken'):
        element = response.html.find('input[name="{}"]'.format(input_name),
                                     first=True)
        post_data[input_name] = element.attrs['value']

    # Get the list of characters from the selection box and get the user to
    # choose
    selection = response.html.find('select[name="CharacterId"] option')
    if character_id is not None:
        post_data['CharacterId'] = str(character_id)
    else:  # pragma: nocover
        choices = []
        for option in selection:
            value = option.attrs.get('value')
            choices.append(value)
            print('{}. {}'.format(len(choices), option.text))

        while 'CharacterId' not in post_data:
            choice = input('Chose character: ')
            try:
                post_data['CharacterId'] = choices[int(choice) - 1]
                break
            except ValueError:
                print('Invalid choice')
            except IndexError:
                print('Invalid choice')

    # Send the request and wait for the redirect to our local http server
    response = response.session.post(ESI_AUTHORIZE_ENDPOINT, data=post_data)
    response.raise_for_status()


def verify_authorization_code(authorization_code, client_id=CLIENT_ID,
                              secret_key=SECRET_KEY):
    authenticator = ESIAuthenticator()
    return authenticator.verify_authorization_code(authorization_code,
                                                   client_id,
                                                   secret_key)


def verify_access_token(access_token):
    authenticator = ESIAuthenticator()
    return authenticator.verify_access_token(access_token)


def get_access_token(refresh_token, client_id=CLIENT_ID,
                     secret_key=SECRET_KEY):
    authenticator = ESIAuthenticator()
    return authenticator.get_access_token(refresh_token,
                                          client_id,
                                          secret_key)


def revoke_token(token, token_type, client_id=CLIENT_ID, secret_key=SECRET_KEY):
    authenticator = ESIAuthenticator()
    return authenticator.revoke_token(token, token_type=token_type,
                                      client_id=client_id, secret=secret_key)
