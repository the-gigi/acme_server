from acme_db import db, models
from acme_service.alien_scanner import locate_alien
from unittest import TestCase


class AlienScannerTest(TestCase):
    def setUp(self):
        db.init('sqlite:///:memory:')
        self.session = db.get_session()
        self.query = self.session.query

    def test_locate_alien(self):
        q = self.query

        assert q(models.Alien).count() == 0
        locate_alien()
        assert q(models.Alien).count() == 1


