"""Generate alien abduction and probe requests"""
from datetime import datetime, timedelta
from time import sleep

class Simulator(object):
    def __init__(self, duration, delay, acme_url):
        assert isinstance(duration, timedelta)
        assert isinstance(delay, timedelta)

        self.duration = duration
        self.delay = delay


class Simulator(object):
    def __init__(self, duration, delay_in_seconds, acme_url):
        assert isinstance(duration, timedelta)

        self.duration = duration
        self.delay_in_seconds = delay_in_seconds
        self.acme_url = acme_url

    def run(self):
        start = datetime.now()
        end = start + self.duration

        while datetime.now() < end:
            request = self._generate_request()
            self._send_request(request)
            sleep(self.delay_in_seconds)

    def _send_request(self, request):
        raise NotImplementedError

    def _generate_request(self):
        raise NotImplementedError
