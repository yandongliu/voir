from models.base import session
from models import Event
from mappers.event import EventMapper


class EventRepository(object):

    EventTable = Event.__table__

    @classmethod
    def read_one(cls, uuid):
        query = cls.EventTable.select().where(EventTable.c.uuid == uuid)
        rows = session.execute(query)
        if rows:
            entities = map(EventMapper.to_entity_from_obj, list(rows))
            return entities[0]

    @classmethod
    def read_all(cls):
        query = cls.EventTable.select()
        rows = session.execute(query)
        if rows:
            entities = map(EventMapper.to_entity_from_obj, list(rows))
            return entities

    @classmethod
    def write_one(cls, event):
        event.validate()
        query = cls.EventTable.insert().values(
            EventMapper.to_record(event)
        )
        session.execute(query)
