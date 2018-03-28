import unittest
from esy.client import ESIClient, ESIPageGenerator
from esy.exceptions import ESIError, ESIAuthorizationError

VITTOROS = 941287462
EVOLUTION = 144749962


class DummyCache(object):
    def __init__(self):
        self.dummy = {}
        self.hits = 0

    def get(self, key):
        if key in self.dummy:
            self.hits += 1
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
        self.client = ESIClient.get_client('test')
        self.cache = DummyCache()

    def test_get_client(self):
        self.assertIsInstance(self.client, ESIClient)

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
