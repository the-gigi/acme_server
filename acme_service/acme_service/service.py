from acme_db import db
from random import random
from acme_db import models


class AlienAbductionManager(object):
    def __init__(self):
        self.session = db.get_session()

    def get_aliens(self, start, end):
        """Get aliens that were scanned into the system

        :param datetime start:
        :param datetime end:

        Return only aliens who were scanned in the given time range
        """
        pass

    def abduct_alien(self, alien_name):
        """Abduct an alien

        An abduction may or may not succeed.
        If the alien is not in the DB or already abducted
        raise an exception
        """
        q = self.session.query
        a = q(models.Alien).filter_by(name=alien_name, abducted=False).scalar()
        if not a:
            raise Exception('Alien is not in DB or already abducted')
        # Try to abduct alien (78% of failure)
        if random() < 0.78:
            return False

        a.abducted = True
        self.session.commit()
        return True

    def probe_alien(self, alien_name):
        """Probe an abducted alien

        Target alien must be in DB, abducted but not probed yet.
        If any of these requirements is violated an exception will be raised.

        A probe generate a ProbeReport record
        """
        q = self.session.query
        a = q(models.Alien).filter_by(name=alien_name,
                                      abducted=True,
                                      probed=False).scalar()
        if not a:
            raise Exception('Alien is not in DB or not abducted ' +
                            'or probed already')

        a.probed = True
        report = models.ProbeReport()
        report.alien = a
        report.info = 'bla bla bla'

        self.session.commit()



