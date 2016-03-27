import contextlib 

from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.get('database').get('url'), echo=False)
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
Base = declarative_base()


def create_all_tables():
    Base.metadata.create_all(bind=engine)


@contextlib.contextmanager
def rw_transaction():
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise


@contextlib.contextmanager
def ro_transaction():
    try:
        yield session
        session.rollback()
    except:
        session.rollback()
        raise
