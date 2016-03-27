from __future__ import absolute_import

from fabric.api import task, local
from fabric.colors import green, red, magenta
import sqlalchemy_utils

from models.base import engine, create_all_tables,  session
from models.mytable import MyTable

@task
def hello():
    print green('hi')

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
    rows = session.query(MyTable).all()
    for row in rows:
        print row.id, row.name

@task
def fake_item(environment='development'):
    """Create fake item."""

    print green('Fake items')
    new_record = MyTable('Hello', 'World')
    session.add(new_record)
    # session.execute("insert into MyTable (name, value) values ('hello', 'world')")
    session.commit()

@task
def serve():
    local('python app.py')
