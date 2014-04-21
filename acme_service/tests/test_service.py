from acme_db import db, models
from acme_service.service import AlienAbductionManager

from unittest import TestCase


class ServiceTest(TestCase):
    def setUp(self):
        db.init('sqlite:///:memory:')
        self.session = db.get_session()
        self.query = self.session.query

        # Add 5 aliens to the DB
        for i in range(5):
            a = models.Alien()
            a.name = 'alien_' + str(i)
            self.session.add(a)

        self.session.commit()
        self.manager = AlienAbductionManager()
        self.manager.session = self.session

    def test_get_aliens(self):
        aliens = self.manager.get_aliens()
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
        aa = s.query(models.Alien).filter_by(name='alien_3',
                                             abducted=True).scalar()
        self.assertIsNotNone(aa)

    def test_probe_alien(self):
        # Artificially "abduct" an alien
        q = self.query
        a = q(models.Alien).filter_by(name='alien_2').one()
        a.abducted = True
        self.session.commit()

        a = q(models.Alien).filter_by(name='alien_2').one()
        self.assertTrue(a.abducted)
        self.assertFalse(a.probed)

        # Verify there are no probe reports yet
        self.assertEqual(0, q(models.ProbeReport).count())

        # Probe the alien
        self.manager.probe_alien('alien_2')

        a = q(models.Alien).filter_by(name='alien_2').one()
        self.assertTrue(a.abducted)
        self.assertTrue(a.probed)

        report = q(models.ProbeReport).get(a.id)
        self.assertIsNotNone(report)
