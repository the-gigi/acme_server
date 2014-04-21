from acme_db import db, models
from acme_service.service import AlienAbductionManager

from unittest import TestCase
from datetime import datetime, timedelta


class ServiceTest(TestCase):
    def setUp(self):
        db.init('sqlite:///:memory:')
        self.session = db.get_session()
        self.query = self.session.query

        self.start = datetime.utcnow() - timedelta(seconds=10)
        # Add 5 aliens to the DB
        for i in range(5):
            a = models.Alien()
            a.name = 'alien_' + str(i)
            a.created = self.start + timedelta(seconds=i)
            self.session.add(a)

        self.session.commit()
        self.manager = AlienAbductionManager()
        self.manager.session = self.session

    def test_get_aliens(self):
        aliens = self.manager.get_aliens(self.start,
                                         self.start + timedelta(seconds=7))
        self.assertEqual(5, len(aliens))

    def test_abduct_alien(self):
        q = self.query
        # a = q(models.Alien).filter_by(name='alien_3').one()
        # self.assertFalse(a.abducted)

        abducted = False
        while not abducted:
            abducted = self.manager.abduct_alien('alien_3')

        # Use new session
        s = db.get_session()
        aa = s.query(models.Alien).filter(
            (models.Alien.name == 'alien_3') &
            (models.Alien.abducted is not None)).scalar()
        self.assertIsNotNone(aa)

    def test_probe_alien(self):
        # Artificially "abduct" an alien
        q = self.query
        a = q(models.Alien).filter_by(name='alien_2').one()
        a.abducted = self.start + timedelta(seconds=8)
        self.session.commit()

        # Use new session
        s = db.get_session()
        q = s.query
        a = q(models.Alien).filter_by(name='alien_2').one()
        self.assertIsNotNone(a.abducted)
        # Verify there are no probe reports yet
        self.assertEqual(0, q(models.ProbeReport).count())

        # Probe the alien
        self.manager.probe_alien('alien_2')

        a = q(models.Alien).filter_by(name='alien_2').one()
        self.assertIsNotNone(a.abducted)
        s = db.get_session()
        q = s.query
        report = q(models.ProbeReport).filter_by(alien=a).scalar()
        self.assertIsNotNone(report)
