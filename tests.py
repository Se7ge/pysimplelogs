import unittest
import os
import json

import requests

from pysimplelogs import get_levels_list


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

if __name__ == '__main__':
    unittest.main()