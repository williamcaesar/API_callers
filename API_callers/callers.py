# -*- coding: utf-8 -*-

import requests


class SyncCaller:
    """Call a set of API calls asynchronously."""
    def __init__(self, headers, payloads, url):
        self.url = url
        self.headers = headers
        self.payloads = payloads
        self.responses = list()

    def send(self):
        for payload in self.payloads:
            response = requests.post(self.url, json=payload, headers=self.headers)
            self.responses.append({'payload': payload,
                                   'response': response})
        return self.responses

    @property
    def results(self):
        return self.send()


