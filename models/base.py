import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.get('database').get('url'), echo=False)
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

class Base(object):

    def to_dict(self):
        if not self.attrs:
            raise Exception('No attrs defined')
        desp = {}
        for attr in self.attrs:
            value = getattr(self, attr)
            desp[attr] = value

        return desp

Model = declarative_base(cls=Base)

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
