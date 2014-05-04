import json
import os
import sys
from acme_db import db, models
from acme_service.service import AlienAbductionManager

from unittest import TestCase
from datetime import datetime, timedelta
import test_config
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))
from api import create_app


class ServiceTest(TestCase):
    def setUp(self):
        # Get rid of old test DB if any
        db_filename = test_config.DB_FILENAME
        if os.path.isfile(db_filename):
            os.remove(db_filename)

        app = create_app(test_config)
        self.test_app = app.test_client()
        self.session = db.get_session()

    def test_get_aliens(self):
        self.start = datetime.utcnow() - timedelta(seconds=10)
        # Add 5 aliens to the DB
        for i in range(5):
            a = models.Alien()
            a.name = 'alien_' + str(i)
            a.created = self.start + timedelta(seconds=i)
            self.session.add(a)

        self.session.commit()

        response = self.test_app.get('/v1/aliens')
        aliens = json.loads(response.data)['result']
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
