from __future__ import absolute_import

import random

from fabric.api import task, local
from fabric.colors import green, red, magenta
import sqlalchemy_utils

from lib import util
from models.base import (
    create_all_tables,
    engine,
    ro_transaction,
    rw_transaction,
)
from models.mytable import MyTable


@task
def bootstrap_database(environment='development'):
    """Create the database."""
    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)
    else:
        print green('Database {} already exists'.format(engine.url.database))

@task
def drop_database(environment='development'):
    """Drop the database."""
    if sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.drop_database(engine.url)
    else:
        print green('Database {} doesn\'t exists'.format(engine.url.database))

@task
def create_tables(environment='development'):
    """Create all tables."""
    create_all_tables()

@task
def drop_table(table):
    """Drop the database."""

    print green('Dropping table %s' % table)
    Session.execute('drop table %s' % table)
    Session.commit()

@task
def print_database(environment='development'):
    """print the database."""

    print green('Printing database')
    with ro_transaction() as session:
        rows = session.query(MyTable).all()
        for row in rows:
            print row.id, row.name, row.value

@task
def fake_item(environment='development'):
    """Create fake item."""

    print green('Fake items')
    def random_text():
        return ''.join([random.choice(list('abcdefghijklmnopqrstuvwxyz')) for _ in xrange(7)])
    with rw_transaction() as session:
        new_record = MyTable('Hello', util.random_string())
        print 'Inserting {}'.format(new_record)
        session.add(new_record)

@task
def serve():
    local('python app.py')
