import unittest
import os
import json

import requests

from pysimplelogs import get_levels_list, Simplelog


class TestGetLevelsFunction(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000"
        self.levels_dict_local = {u'level': [u'critical', u'error', u'warning', u'notice', u'info', u'debug']}

    def test_server_available(self):
        levels_dict = get_levels_list(self.url)
        levels_list_from_server = json.loads(requests.get(os.path.join(self.url + "/api/level/")).content)
        self.assertEqual(levels_list_from_server, levels_dict, 'Server unavailable.')

    def test_server_unavailable(self):
        levels_dict = get_levels_list(self.url)
        self.assertEqual(self.levels_dict_local, levels_dict, 'Levels list in library are not as default.')


class TestGetData(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000"
        self.simplelog = Simplelog(self.url)
        self.simplelog.error({'ip': '127.0.0.1', 'name': 'Test'}, "This is a test!", ["simplelogs", "test"])
        self.simplelog.warning({'ip': '127.0.0.1', 'name': 'Test'}, "This is a test!", ["simplelogs", "test"])
        self.simplelog.info({'ip': '127.0.0.1', 'name': 'Test'}, "This is a test!", ["simplelogs", "test"])

    def test_get_owners(self):
        owners = self.simplelog.get_owners()
        self.assertIsNotNone(owners)
        self.assertTrue(owners['OK'])
        self.assertIn({'ip': '127.0.0.1', 'name': 'Test'}, owners['result'])

    def test_get_list(self):
        result = self.simplelog.get_list(find=dict(level='error', owner='Test'))
        self.assertIsNotNone(result)
        self.assertTrue(result['OK'])
        entry = result['result'][0]
        self.assertTrue('OK' in result and
                        result['OK'] and
                        entry['level'] == 'error' and
                        entry['owner'] == {'ip': '127.0.0.1', 'name': 'Test'} and
                        entry['data'] == "This is a test!" and
                        entry['tags'] == ["simplelogs", "test"],
                        msg="Server response is not the same as entry in DB.")

    def test_count(self):
        count = self.simplelog.count(find=dict(level='warning', owner='Test'))
        self.assertIsNotNone(count)
        self.assertTrue(count['OK'])
        self.assertGreaterEqual(count['result'], 1)


if __name__ == '__main__':
    unittest.main()