from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import metadata
import models


get_session = None
engine = None


def init(db_uri):
    print 'db.init() here'
    global get_session
    global engine
    engine = create_engine(db_uri)
    metadata.create_all(engine)
    get_session = sessionmaker(bind=engine)
    q = get_session().query
    assert q(models.Alien).all() == []



