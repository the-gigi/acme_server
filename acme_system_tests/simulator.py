"""Generate alien abduction and probe requests"""
from datetime import datetime, timedelta


class Simulator(object):
    def __init__(self, duration, delay, acme_url):
        assert isinstance(duration, timedelta)
        assert isinstance(delay, timedelta)

        self.duration = duration
        self.delay = delay
        self.acme_url = acme_url

    def run(self):
        start = datetime.now()
        end = start + self.duration

        while datetime.now() < end:
            request = self._generate_request()
            self._send_request()

    def _send_request(self):
        raise NotImplementedError

    def _generate_request(self):
        raise NotImplementedError
