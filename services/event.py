from datetime import datetime
from uuid import uuid4

from entities import Event
from services.repositories.event import EventRepository

class EventService(object):

    @classmethod
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
        EventRepository.write_one(event)
        return event
