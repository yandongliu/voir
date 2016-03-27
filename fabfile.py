from __future__ import absolute_import

from fabric.api import task, local
from fabric.colors import green, red, magenta

from models import database
from models.session import Session
from models.item import Item

@task
def hello():
    print green('hi')

@task
def bootstrap_database(environment='development'):
    """Create the database."""

    print green('Dropping database')
    database.drop()
    print green('Creating database')
    database.create()
    print green('Defining schema')
    with open('migrations/schema.sql') as f:
        sql = f.read().replace('\n', '')
    Session.execute(sql)
    Session.commit()

@task
def drop_database(environment='development'):
    """Drop the database."""

    print green('Dropping database')
    # database.drop()
    # import pdb; pdb.set_trace()
    Session.execute('drop database %s' % Session.bind.url.database)

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
    rows = Session.query(Item).all()
    for row in rows:
        print row.id, row.name

@task
def fake_items(environment='development'):
    """Create the database."""

    print green('Fake items')
    Session.execute("insert into item (name) values ('hello')")
    Session.execute("insert into item (name) values ('world')")
    Session.commit()

@task
def serve():
    local('python app.py')
