from app.mappers.event import EventMapper
from app.models import Event
from app.services.repositories.base import BaseRepository, BaseRepositoryAsync


class EventRepository(BaseRepository):

    Table = Event.__table__
    Mapper = EventMapper


class EventRepositoryAsync(BaseRepositoryAsync):

    Table = Event.__table__
    Mapper = EventMapper
