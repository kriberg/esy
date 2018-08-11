import unittest
import os
import os.path
import json
from collections import defaultdict
from esy.client import ESIClient, ESIPageGenerator
from esy.entities import Character, Corporation, Entity, Alliance
from esy.exceptions import ESIError, ESIAuthorizationError, ESIForbidden
import esy.devel

VITTOROS = 941287462
EVOLUTION = 144749962


class DummyCache(object):
    def __init__(self):
        self.dummy = {}
        self.hits = 0
        self.key_hits = defaultdict(lambda: 0)

    def get(self, key):
        if key in self.dummy:
            self.hits += 1
            self.key_hits[key] += 1
        return self.dummy.get(key)

    def set(self, key, data, *args):
        self.dummy[key] = data

    def clear(self):
        self.dummy.clear()

    def __len__(self):
        return len(self.dummy)

    def __contains__(self, item):
        return item in self.dummy


class TestESIClient(unittest.TestCase):
    def setUp(self):
        spec_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'swagger.json')
        with open(spec_path, 'r') as spec_file:
            spec = json.load(spec_file)
        self.client = ESIClient.get_client(spec=spec)
        self.cache = DummyCache()

    def test_get_client(self):
        self.assertIsInstance(self.client, ESIClient)
        self.assertIsInstance(ESIClient.get_client(),
                              ESIClient)

    def test_spec_parsing(self):
        spec = ESIClient.get_swagger_spec()
        self.assertIn('paths', spec)
        self.assertIsInstance(spec['paths'], dict)
        namespaces = set()

        for path in spec['paths']:
            for method in spec['paths'][path]:
                namespaces.add(spec['paths'][path][method]['tags'][0])

        for namespace in namespaces:
            self.assertTrue(hasattr(self.client, namespace))

        with self.assertRaises(ESIError):
            ESIClient.get_swagger_spec(endpoint='https://localhost/')

        with self.assertRaises(AttributeError):
            self.client.Foo.bar()
        with self.assertRaises(AttributeError):
            self.client.Character.bar()

        size1 = len(self.cache)
        spec1 = ESIClient.get_swagger_spec(cache=self.cache)
        size2 = len(self.cache)
        spec2 = ESIClient.get_swagger_spec(cache=self.cache)
        size3 = len(self.cache)
        self.assertDictEqual(spec1, spec2)
        self.assertTrue(size1 + 1 == size2)
        self.assertTrue(size2 == size3)

    def test_alliance(self):
        alliances = self.client.Alliance.get_alliances()
        self.assertIsInstance(alliances, list)
        self.assertTrue(len(alliances) > 100)

    def test_pagination(self):
        types_generator = self.client.Universe.get_universe_types()
        self.assertIsInstance(types_generator, ESIPageGenerator)
        batch = next(types_generator)
        self.assertIsInstance(batch, list)
        self.assertTrue(len(batch) == 1000)
        self.assertTrue(types_generator.page > 1)
        self.assertTrue(types_generator.num_pages > 30)
        types_generator.page = types_generator.num_pages
        batch = next(types_generator)
        self.assertIsInstance(batch, list)
        self.assertTrue(len(batch) < 1000)
        with self.assertRaises(StopIteration):
            next(types_generator)

        self.assertIsInstance(types_generator.__iter__(), ESIPageGenerator)

    def test_post(self):
        names = ('Vittoros',
                 'Evolution',
                 'Northern Coalition.')
        ids = self.client.Universe.post_universe_ids(names=names)
        self.assertIsInstance(ids, dict)
        self.assertIsInstance(ids['characters'], list)
        self.assertTrue(len(ids['characters']), 1)
        self.assertTrue(len(ids['corporations']), 1)
        self.assertTrue(len(ids['alliances']), 1)
        self.assertTrue(ids['characters'][0]['id'] == VITTOROS)
        self.assertTrue(ids['corporations'][0]['id'] == EVOLUTION)

    def test_missing_token(self):
        with self.assertRaises(ESIAuthorizationError):
            self.client.Character.get_characters_character_id_blueprints(
                character_id=VITTOROS
            )
        with self.assertRaises(ESIForbidden):
            gen = self.client.Character.get_characters_character_id_blueprints(
                character_id=VITTOROS,
                _token='hunter2'
            )
            next(gen)

    def test_with_token(self):
        alliances = self.client.Alliance.get_alliances(_token='Foo')
        self.assertIsInstance(alliances, list)
        self.assertTrue(len(alliances) > 100)

    def test_caching(self):
        self.cache.clear()
        self.client.cache = self.cache
        self.assertIsInstance(self.client.cache, DummyCache)
        self.assertTrue(len(self.cache) == 0)
        status1 = self.client.Status.get_status()
        self.assertTrue(len(self.cache) == 1)
        self.assertTrue(self.cache.hits == 0)
        status2 = self.client.Status.get_status()
        self.assertTrue(self.cache.hits == 1)
        self.assertEqual(status1, status2)


@unittest.skipIf('TRAVIS' in os.environ,
                 'Skipping auth flow tests on travis-ci')
class TestDevel(unittest.TestCase):
    def setUp(self):
        self.test_username = os.getenv('ESY_TEST_USERNAME')
        self.test_password = os.getenv('ESY_TEST_PASSWORD')  # hunter2
        self.test_character_id = os.getenv('ESY_CHARACTER_ID')
        self.client_id = os.getenv('ESY_CLIENT_ID')
        self.secret_key = os.getenv('ESY_SECRET_KEY')
        self.scopes = os.getenv('ESY_SCOPES')

    def test_authorization_flow(self):
        if not all((self.test_username, self.test_password, self.client_id,
                    self.scopes, self.test_character_id)):
            self.skipTest('Missing authorization parameters.')
        authorization_code = esy.devel.get_authorization_code(
            cli_login=True,
            client_id=self.client_id,
            scopes=self.scopes,
            character_id=self.test_character_id,
            username=self.test_username,
            password=self.test_password)
        self.assertIsInstance(authorization_code, str)
        self.assertTrue(len(authorization_code) == 65)

        refresh_token, access_token = esy.devel.verify_authorization_code(
            authorization_code, client_id=self.client_id,
            secret_key=self.secret_key)

        self.assertIsInstance(refresh_token, str)
        self.assertTrue(len(refresh_token) == 65)
        self.assertIsInstance(access_token, str)
        self.assertTrue(len(access_token) == 87)

        char_info = esy.devel.verify_access_token(access_token)
        self.assertIsInstance(char_info, dict)
        self.assertIn('CharacterID', char_info)
        self.assertIn('CharacterName', char_info)
        self.assertIn('CharacterOwnerHash', char_info)
        self.assertEqual(str(char_info.get('CharacterID')),
                         self.test_character_id)

        new_access_token = esy.devel.get_access_token(
            refresh_token, client_id=self.client_id, secret_key=self.secret_key)
        self.assertIsInstance(new_access_token, str)
        self.assertTrue(len(new_access_token) == 87)

        for token, token_type in ((new_access_token, 'access_token'),
                                  (access_token, 'access_token'),
                                  (refresh_token, 'refresh_token')):
            status = esy.devel.revoke_token(token,
                                            token_type=token_type,
                                            client_id=self.client_id,
                                            secret_key=self.secret_key)
            self.assertTrue(status)


class TestEntities(unittest.TestCase):
    def setUp(self):
        spec_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'swagger.json')
        with open(spec_path, 'r') as spec_file:
            spec = json.load(spec_file)
        self.cache = DummyCache()
        self.client = ESIClient.get_client(spec=spec, cache=self.cache)
        self.test_charname = os.getenv('ESY_TEST_CHARACTER')
        self.test_username = os.getenv('ESY_TEST_USERNAME')
        self.test_password = os.getenv('ESY_TEST_PASSWORD')  # hunter2
        self.test_character_id = os.getenv('ESY_CHARACTER_ID')
        self.client_id = os.getenv('ESY_CLIENT_ID')
        self.secret_key = os.getenv('ESY_SECRET_KEY')
        self.scopes = os.getenv('ESY_SCOPES')

    def do_login(self):
        if not all((self.test_username, self.test_password, self.client_id,
                    self.scopes, self.test_character_id)):
            self.skipTest('Missing authorization parameters.')
        authorization_code = esy.devel.get_authorization_code(
            cli_login=True,
            client_id=self.client_id,
            scopes=self.scopes,
            character_id=self.test_character_id,
            username=self.test_username,
            password=self.test_password)
        refresh_token, access_token = esy.devel.verify_authorization_code(
            authorization_code, client_id=self.client_id,
            secret_key=self.secret_key)
        self.refresh_token = refresh_token
        self.access_token = access_token

    def do_logout(self):
        for token, token_type in ((self.access_token, 'access_token'),
                                  (self.refresh_token, 'refresh_token')):
            esy.devel.revoke_token(token,
                                   token_type=token_type,
                                   client_id=self.client_id,
                                   secret_key=self.secret_key)

    def test_public_entities(self):
        vitt = Character(VITTOROS, _client=self.client)
        self.assertEqual(vitt.id, VITTOROS)
        self.assertEqual(vitt.name, 'Vittoros')
        with self.assertRaises(AttributeError):
            _ = vitt.elite
        evol = Corporation(EVOLUTION, _client=self.client)
        self.assertEqual(evol.id, EVOLUTION)
        self.assertEqual(evol.name, 'Evolution')

        self.assertIsInstance(vitt.corporation, Corporation)
        self.assertEqual(vitt.corporation.name, 'Evolution')
        self.assertEqual(vitt.corporation.id, EVOLUTION)
        self.assertTrue(vitt.corporation == evol)

        ccp = Entity.from_name('C C P Alliance', _client=self.client)
        self.assertIsInstance(ccp, Alliance)

        self.assertIn('get_blueprints', dir(vitt))
        self.assertIn('security_status', dir(vitt))

    @unittest.skipIf('TRAVIS' in os.environ,
                     'Skipping authed tests on travis-ci.')
    def test_authed_character(self):
        self.do_login()
        char = Character(self.test_character_id, _token=self.access_token)
        self.assertIsInstance(char.get_blueprints(), ESIPageGenerator)
        self.do_logout()
