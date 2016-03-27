import contextlib

from sqlalchemy import create_engine
engine = create_engine('mysql://tornado_user:qwerty123!@localhost:3306/tornado_app', echo=False)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.ext.declarative import declarative_base

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
