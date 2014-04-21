from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import metadata

get_session = None


def init(db_uri):
    global get_session
    engine = create_engine(db_uri)
    metadata.create_all(engine)
    get_session = sessionmaker(bind=engine)



