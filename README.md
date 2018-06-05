# Introduction
**************

[![Build Status](https://travis-ci.org/kriberg/esy.svg?branch=master)](https://travis-ci.org/kriberg/esy)
[![Coverage Status](https://coveralls.io/repos/github/kriberg/esy/badge.svg?branch=master)](https://coveralls.io/github/kriberg/esy?branch=master)
[![Documentation Status](https://readthedocs.org/projects/esy/badge/?version=latest)](https://esy.readthedocs.io/en/latest/?badge=latest)

There are many options for consuming the ESI web services. ESY aims to be an easy-to-use library with the nuts and 
bolts of dealing with an OpenAPI interface abstracted away. ESY was created to have an interface reminscient of Entity's
gloriously pythonic [eveapi](https://github.com/ntt/eveapi/) library and to 

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


# Get paginated asset list
swag =  client.Corporation.get_corporations_corporation_id_assets(corporation_id=144749962,
                                                                  _token='esi token')
# Loop through the asset pages
for page in swag:
    for asset in page:
       print(asset.get('type_id'),
             asset.get('location_id'))
       # 22457
       # 16074150552
```



## Development

ESY uses the [Bravado](https://github.com/Yelp/bravado-core) OpenAPI library to parse the ESI swagger schema and create
an usable interface. The purpose of creating a custom wrapper of Bravado for ESI, is to make the interface a bit more 
user friendly. Pagination is handled automatically by returning generators for any route which accepts a page 
parameter, while non-paginated data is handled in their native data type. Tokens can be set per-call, instead of 
per-client, allowing for using headers and still getting data for many tokens without the ned to reinitialize the client.
