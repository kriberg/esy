#!/usr/bin/env python
import os.path
import sys
import json
from esy.client import ESIClient

PARAM_TYPES = {
    'integer': 'int',
    'string': 'str',
    'array': 'list',
    'object': 'dict'
}

INDEX_HEADER = '''ESI API
#######

.. toctree::
   :maxdepth: 4
   :caption: Namespaces

.. autosummary::
   :toctree: generated
   
'''


def t(text, indent):
    return text.rjust(len(text) + indent)


def ptype(param_type):
    return PARAM_TYPES.get(param_type, param_type)


def generate_operation_doc(name, operation):
    print(f'\tAdding {name}...')
    op_spec = operation.operation.op_spec
    summary = op_spec.get('summary')
    signature = []
    for param_name, spec in operation.operation.params.items():
        if spec.required:
            signature.append(param_name)
        else:
            if param_name in ('datasource', 'If_None_Match', 'page', 'token'):
                continue
            default = spec.param_spec.get('default')
            if spec.param_spec.get('type') == 'string' and default is not None:
                default = f"'{default}'"
            signature.append(f'[{param_name}={default}]')

    if operation.require_authorization:
        signature.append('[_token=None]')
    yield t(f'.. py:method:: {name}({", ".join(signature)})\n\n', 3)
    yield t(f'{summary}\n\n', 3)

    for param_name, spec in operation.operation.params.items():
        if param_name in ('datasource', 'If_None_Match', 'page', 'token'):
            continue
        param_type = ptype(spec.param_spec.get('type'))
        param_desc = spec.param_spec.get('description')
        yield t(f':param {param_type} {param_name}: {param_desc}\n', 6)
    if operation.require_authorization:
        yield t(':param str _token: ESI authorization token\n', 6)
    ok_response = op_spec.get('responses', {}).get('200', {})
    rdesc = ok_response.get('description')
    rtype = ptype(ok_response.get('schema', {}).get('type'))
    if operation.paginated:
        yield t(f':return: {rdesc}\n', 6)
        yield t(f':rtype: :class:`~esy.client.ESIPageGenerator` {rtype}\n', 6)
    else:
        yield t(f':return: {rdesc}\n', 6)
        yield t(f':rtype: {rtype}\n', 6)
    yield '\n\n'


def generate_namespace_doc(namespace, resource):
    print(f'Generating docs for {namespace}...')
    yield f'{namespace}\n'
    yield f'{"-" * len(namespace)}\n\n'
    yield f'.. py:class:: {namespace}\n\n'

    for name in dir(resource):
        operation = getattr(resource, name)
        for output in generate_operation_doc(name, operation):
            yield output
    yield '\n\n'


def update_docs():
    basedir = os.path.dirname(os.path.realpath(__file__))
    spec_path = os.path.join(basedir, 'tests', 'swagger.json')

    if not os.path.exists(spec_path):
        print('No swagger spec present. Download it first.')
        sys.exit(-1)

    with open(spec_path, 'r') as spec_file:
        spec = json.load(spec_file)
        client = ESIClient.get_client('esy tests', spec=spec)

    doc_path = os.path.join(basedir, 'doc', 'source', 'esi.rst')

    with open(doc_path, 'w') as index:
        index.write(INDEX_HEADER)

        for namespace in sorted(dir(client)):
            resource = getattr(client, namespace)
            for output in generate_namespace_doc(namespace, resource):
                index.write(output)


if __name__ == '__main__':
    update_docs()
