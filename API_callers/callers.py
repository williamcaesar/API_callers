# -*- coding: utf-8 -*-

import requests

from abc import ABC


class Caller(ABC):
    def __init__(self, headers, payloads, url):
        self.url = url
        self.headers = headers
        self.payloads = payloads
        self.responses = list()

    @property
    def results(self):
        pass


class SyncCaller(Caller):
    """
    Call a set of API calls asynchronously.
    """
    def _build(self, payload):
        if type(payload) == dict and 'metadata' in payload.keys():
            metadata = payload['metadata']
            payload.pop('metadata')
        else:
            metadata = None
        response = requests.post(self.url, json=payload, headers=self.headers)
        return {'payload': payload, 'response': response, 'metadata': metadata}

    def send(self):
        self.responses = [self._build(x) for x in self.payloads]
        return self.responses

    @property
    def results(self):
        return self.send()


