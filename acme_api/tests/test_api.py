import json
import os
import sys
from acme_db import db, models

from unittest import TestCase
from datetime import datetime, timedelta
import config
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))
from api import create_app


class ServiceTest(TestCase):
    def setUp(self):
        # Get rid of old test DB if any
        db_filename = config.DB_FILENAME
        if os.path.isfile(db_filename):
            os.remove(db_filename)

        app = create_app(config)
        self.test_app = app.test_client()
        self.session = db.get_session()

        self.start = datetime.utcnow() - timedelta(seconds=10)
        # Add 5 aliens to the DB
        for i in range(5):
            a = models.Alien()
            a.name = 'alien_' + str(i)
            a.created = self.start + timedelta(seconds=i)
            self.session.add(a)

        self.session.commit()

    def test_get_aliens(self):
        response = self.test_app.get('/v1/aliens')
        aliens = json.loads(response.data)['result']
        self.assertEqual(5, len(aliens))

    def test_get_report(self):
        q = self.session.query
        alien = q(models.Alien).filter_by(name='alien_3').one()
        r = models.ProbeReport()
        r.alien = alien
        r.created = self.start + timedelta(seconds=8)
        r.info = 'blah blah'
        self.session.add(r)
        self.session.commit()

        response = self.test_app.get('/v1/report?alien_name=alien_3')
        report = json.loads(response.data)['result']
        self.assertEqual('blah blah', report['info'])
