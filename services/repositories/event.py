from mappers.event import EventMapper
from models import Event
from services.repositories.base import BaseRepository


class EventRepository(BaseRepository):

    Table = Event.__table__
    Mapper = EventMapper
