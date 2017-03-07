from tornado.gen import coroutine, Return
from tornado.concurrent import run_on_executor, futures
from tornado.ioloop import IOLoop

from app.lib.async import runner
from app.models.base import ro_transaction, rw_transaction, session as sess


class BaseRepository(object):

    @classmethod
    def read_one(cls, uuid):
        query = cls.Table.select().where(cls.Table.c.uuid == uuid)
        rows = sess.execute(query)
        if rows:
            entities = map(cls.Mapper.to_entity_from_obj, list(rows))
            return entities[0]

    @classmethod
    def read_many(cls, limit=None):
        query = cls.Table.select()
        if limit:
            query = query.limit(limit)
        rows = sess.execute(query)
        if rows:
            entities = map(cls.Mapper.to_entity_from_obj, list(rows))
            return entities

    @classmethod
    def write_one(cls, entity):
        entity.validate()
        query = cls.Table.insert().values(cls.Mapper.to_record(entity))
        sess.execute(query)
        sess.commit()


class BaseRepositoryAsync(object):

    @classmethod
    @runner.async
    def read_one(cls, uuid):
        with ro_transaction() as session:
            query = cls.Table.select().where(cls.Table.c.uuid == uuid)
            rows = session.execute(query)
            if rows:
                entities = map(cls.Mapper.to_entity_from_obj, list(rows))
                return entities[0]

    @classmethod
    @runner.async
    def read_many(cls, limit=None):
        with ro_transaction() as session:
            query = cls.Table.select()
            if limit:
                query = query.limit(limit)
            rows = session.execute(query)
            if rows:
                entities = map(cls.Mapper.to_entity_from_obj, list(rows))
                return entities

    @classmethod
    @runner.async
    def write_one(cls, entity):
        with rw_transaction() as session:
            entity.validate()
            query = cls.Table.insert().values(cls.Mapper.to_record(entity))
            session.execute(query)
            session.commit()
