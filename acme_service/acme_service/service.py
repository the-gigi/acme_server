from random import random
from datetime import datetime
from acme_db import db
from acme_db import models


class AlienAbductionManager(object):
    def __init__(self):
        pass

    def get_aliens(self, start, end):
        """Get aliens that were scanned into the system

        :param datetime start:
        :param datetime end:

        Return only aliens who were scanned in the given time range
        """
        q = db.get_session().query
        m = models.Alien
        return q(m).filter((start <= m.created) & (m.created < end)).all()

    def abduct_alien(self, alien_name):
        """Abduct an alien

        An abduction may or may not succeed.
        If the alien is not in the DB or already abducted
        raise an exception
        """
        s = db.get_session()
        q = s.query
        a = q(models.Alien).filter_by(name=alien_name, abducted=None).scalar()
        if not a:
            raise Exception('Alien is not in DB or already abducted')
        # Try to abduct alien (78% of failure)
        if random() < 0.78:
            return False

        a.abducted = datetime.utcnow()
        s.commit()
        return True

    def probe_alien(self, alien_name):
        """Probe an abducted alien

        Target alien must be in DB, abducted but not probed yet.
        If any of these requirements is violated an exception will be raised.

        A probe generate a ProbeReport record
        """
        s = db.get_session()
        q = db.get_session().query
        m = models.Alien
        a = q(m).filter((m.name == alien_name) &
                        (m.abducted is not None)).scalar()
        if not a:
            raise Exception('Alien is not in DB or not abducted yet')

        report = q(models.ProbeReport).filter_by(alien=a).scalar()
        if report:
            raise Exception('Alien has already been probed')

        report = models.ProbeReport()
        report.alien_id = a.id
        report.info = 'bla bla bla'
        report.created = datetime.utcnow()
        s.add(report)
        s.commit()



