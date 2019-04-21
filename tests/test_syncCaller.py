from unittest import TestCase
from requests import Response
from API_callers.callers import SyncCaller


class TestSyncCaller(TestCase):
    def test_send_one(self):
        caller = SyncCaller({'fake': 'headers'},
                            {'payload': 'payloads'},
                            'https://jsonplaceholder.typicode.com/posts')
        response = caller.send()
        self.assertEqual(len(response), 1)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Response)

    def test_send_3(self):
        payloads = [{'payload{}'.format(x): 'payloads'} for x in range(0, 3)]
        caller = SyncCaller({'fake': 'headers'},
                            payloads,
                            'https://jsonplaceholder.typicode.com/posts')
        response = caller.send()
        self.assertGreater(len(response), 1)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Response)
        self.assertIsInstance(response[1], Response)
        self.assertIsInstance(response[2], Response)

    def test_results(self):
        caller = SyncCaller({'fake': 'headers'},
                            {'payload': 'payloads'},
                            'https://jsonplaceholder.typicode.com/posts')
        self.assertEqual(len(caller.results), 1)
        self.assertIsInstance(caller.results, list)
        self.assertIsInstance(caller.results[0], Response)
