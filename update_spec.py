#!/usr/bin/env python
import os.path
import requests
from esy.constants import ESI_ENDPOINT


def download_spec(spec_path, etag_path):
    resp = requests.get(ESI_ENDPOINT)
    resp.raise_for_status()
    with open(spec_path, 'w') as spec_file:
        spec_file.write(resp.text)
    etag = resp.headers.get('etag')
    with open(etag_path, 'w') as etag_file:
        etag_file.write(etag)

    return etag


def spec_is_updated(etag_path):
    with open(etag_path, 'r') as etag_file:
        etag = etag_file.read()
    resp = requests.head(ESI_ENDPOINT)
    resp.raise_for_status()
    return etag != resp.headers.get('etag')


if __name__ == '__main__':
    tests_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'tests')
    spec_path = os.path.join(tests_path,
                             'swagger.json')
    etag_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             '.etag')

    if not os.path.exists(spec_path) or \
            not os.path.exists(etag_path) or \
            spec_is_updated(etag_path):
        etag = download_spec(spec_path, etag_path)
        print(f'Updated swagger spec to {etag}')
    else:
        print('Swagger spec is up to date ')
