from datetime import datetime
from uuid import uuid4

from tornado.gen import coroutine, Return

from app.entities import Event
from app.services.repositories.event import EventRepository
from app.services.repositories.event import EventRepositoryAsync


class EventService(object):

    @classmethod
    @coroutine
    def create(cls, name, latitude, longitude, created_by):
        now = datetime.utcnow()
        event = Event({
            'uuid': str(uuid4()),
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'created_by': created_by,
            'created_at': now,
            'updated_at': now,
        })
        yield EventRepositoryAsync.write_one(event)
        raise Return(event)

    @classmethod
    @coroutine
    def find_by_uuid(cls, uuid):
        event = yield EventRepositoryAsync.read_one(uuid)
        raise Return(event)

    @classmethod
    @coroutine
    def read_many(cls):
        event = yield EventRepositoryAsync.read_many()
        raise Return(event)
