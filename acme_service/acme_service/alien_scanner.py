import base64
import uuid
from acme_db import db, models
import time
import sys


def locate_alien():
    """Locate an alien and add it to the DB

    Locating an alien in this implementation is as simple
    as naming it using a random uuid
    """

    # Generate a name for the alien
    alien_name = base64.urlsafe_b64encode(uuid.uuid4().bytes)

    # Get DB session
    session = db.get_session()

    # Add to DB
    a = models.Alien()
    a.name = alien_name

    session.add(a)
    session.commit()


if __name__ == '__main__':
    # Initialize db
    db_uri = sys.argv[1]
    db.init(db_uri)
    while True:
        locate_alien()
        time.sleep(500)

