# Introduction

[![Build Status](https://travis-ci.org/kriberg/esy.svg?branch=master)](https://travis-ci.org/kriberg/esy)
[![Coverage Status](https://coveralls.io/repos/github/kriberg/esy/badge.svg?branch=master)](https://coveralls.io/github/kriberg/esy?branch=master)
[![Documentation Status](https://readthedocs.org/projects/esy/badge/?version=latest)](https://esy.readthedocs.io/en/latest/?badge=latest)

There are many options for consuming the ESI web services. ESY aims to be an easy-to-use library with the nuts and 
bolts of dealing with an OpenAPI interface abstracted away. 

ESY is inspired by Entity's gloriously pythonic [eveapi](https://github.com/ntt/eveapi/) library. 

## Installation

The latest stable version of ESY is available from PyPI:
```bash
$ pip install esy
```

## Documentation

Documentation is available at [esy.readthedocs.io](https://esy.readthedocs.io/en/latest/).

For documentation of the various ESI routes, ESY also provides a 
[terse list](https://esy.readthedocs.io/en/latest/source/esi.html) of their parameters and return types. Further
information can be explored at the main [ESI documentation site](https://esi.evetech.net/ui)

## Usage

To use ESI, first initialize a client:

```python
from esy.client import ESIClient
client = ESIClient.get_client('my-user-agent')
```

The client can take a second or two to initialize, as the swagger specification is downloaded and parsed. To speed this
up, you can download the specification locally:

```bash
$ curl https://esi.evetech.net/latest/swagger.json -o swagger.json
```

Then initialize the client using the local file:

```python
import json
from esy.client import ESIClient

with open('swagger.json', 'r') as spec_file:
    spec = json.load(spec_file)
client = ESIClient.get_client('my-user-agent', spec=spec)
```

For production instances, keeping the spec in [Redis](https://redis.io) or some other cache is highly recommended.

### Calling ESI routes

Once your client is initialized, you can fetch data:

```python
from esy.client import ESIClient
client = ESIClient.get_client('my-user-agent')

# Get list of alliances
alliances = client.Alliance.get_alliances()

# Get info on a corporation
evolution = client.Corporation.get_corporations_corporation_id(corporation_id=144749962)
print(evolution)

{'alliance_id': 1727758877, 
 'ceo_id': 144509256, 
 'creator_id': 144509256, 
 'date_founded': datetime.datetime(2003, 7, 30, 8, 33, tzinfo=tzutc()), 
 'description': 'Those who cannot adapt become victims of Evolution.', 
 'home_station_id': 60013843, 
 'member_count': 316, 
 'name': 'Evolution', 
 'shares': 1000, 
 'tax_rate': 0.5, 
 'ticker': 'EVOL', 
 'url': 'http://www.eve-evol.com', 
 'faction_id': None}
```

For ESI routes which are paginated, ESY will return a [ESIPageGenerator](source/modules.html#esy.client.ESIPageGenerator) which is a generator yielding the 
native data type of the route.   

```python
# Get paginated asset list
swag =  client.Corporation.get_corporations_corporation_id_assets(corporation_id=144749962,
                                                                  _token='esi token')
# swag is an ESIPageGenerator, implementing the generator interface
# Loop through it to get the asset pages
for page in swag:  # Returns a list of assets
    for asset in page:  # Asset dict 
       print(asset.get('type_id'),
             asset.get('location_id'))
       # 22457
       # 16074150552
```

### Caching

ESY does not implement caching itself, but supports using a cache through a cache proxy object. The proxy needs
to implement the following interface:

```python
class Cache(object):    
    def get(self, key: int) -> object: 
        pass

    def set(self, key: int, data: object, cached_until: datetime.datetime):
        pass

    def __contains__(self, item: object) -> bool:
        pass
```

### Authentication and devel mode

ESY can handle the authentication flow for you:

```python
from esy.auth import ESIAuthenticator

auth = ESIAuthenticator()
refresh_token, access_token = auth.verify_authorization_code('authorization code from esi',
                                                             'your client ID',
                                                             'your secret key')

auth.verify_access_token(access_token)
{'CharacterID': 941287462,
 'CharacterName': 'Vittoros',
 'ExpiresOn': '2018-06-11T19:01:15.182864Z',
 'Scopes': ' ',
 'TokenType': 'Character',
 'CharacterOwnerHash': '**********'}
 
new_access_token = auth.get_access_token(refresh_token, 
                                         'your client ID', 
                                         'your secret key')

auth.revoke_token(refresh_token,
                  'your client ID', 
                  'your secret key')
                  
auth.revoke_token(access_token,
                  'your client ID', 
                  'your secret key',
                  token_type='access_token')
```

To help developers getting started without having to implement the entire authentication
workflow, ESY also implements an ad-hoc web server to get you refresh tokens. You can use
it directly in the python prompt to do some API exploration or you can use it in your tests
to produce refresh or access tokens for testing your ESI calls.

First, create a new application at [https://developers.eveonline.com/](https://developers.eveonline.com/)
with callback URL set to http://localhost:8000 or whichever address and port you'll be 
running the devel server.

```python
import esy.devel

# get_authorization_code has many parameters, but for basic usage:

auth_code = esy.devel.get_authorization_code(client_id='your client ID',
                                             callback_url='your callback URL', 
                                             scopes='your space-delimited scopes')

# This will start the web server in the background (per-default listening on localhost:8000)
# and print the login URL on stdout. After authenticating in your browser, the web server 
# will get redirect from the SSO with the authorization code, then return that.

# For situations where you are not able to reach the network where you are running ESY, 
# you can also use CLI login: 

auth_code = esy.devel.get_authorization_code(cli_login=True,
                                             client_id='your client ID',
                                             callback_url='your callback URL', 
                                             scopes='your space-delimited scopes')

# This will prompt for username and password, then let you pick a character.
# If you are running tests, you can also supply username, password and character_id as 
# keyword arguments to get_authorization_code, in addition to cli_login=True. This will
# automate the entire flow. Remember to revoke your tokens afterwards and for bob's sake; 
# don't display your username and/or password!

# After getting the authorization code, you can get the tokens:

refresh_token, access_token = esy.devel.verify_authorization_code(auth_code,
                                                                  client_id='your client ID',
                                                                  secret_key='your secret key')
# Character info

char_info = esy.devel.verify_access_token(access_token)

# Get your swag
from esy.client import ESIClient
client = ESIClient.get_client('your-user-agent')
assets = client.Assets.get_characters_character_id_assets(
    character_id=char_info.get('CharacterId'), _token=access_token)

for page in assets:
    print(page)
```

The devel mode will use parameters from environment settings, if present:

Parameter | Environment setting | Default
---| --- | ---
CLIENT_ID | ESY_CLIENT_ID | None
SECRET_KEY | ESY_SECRET_KEY | None
SCOPES | ESY_SCOPES | None
CALLBACK_URL | ESY_CALLBACK_URL | http://localhost:8000
SERVER_ADDRESS | ESY_SERVER_ADDRESS | localhost
SERVER_PORT | ESY_SERVER_PORT | 8000
 

## Development

ESY uses the [Bravado](https://github.com/Yelp/bravado-core) OpenAPI library to parse the ESI swagger schema and create
an usable interface. The purpose of creating a custom wrapper of Bravado for ESI, is to make the interface a bit more 
user friendly. Pagination is handled automatically by returning generators for any route which accepts a page 
parameter, while non-paginated data is handled in their native data type. Tokens can be set per-call, instead of 
per-client, allowing for using headers and still getting data for many tokens without the ned to reinitialize the client.

The authentication flow uses [requests-oauthlib](https://github.com/requests/requests-oauthlib).
