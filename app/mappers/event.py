from __future__ import absolute_import

from app.entities.event import Event
from app.mappers.base import EntityMapper


class EventMapper(EntityMapper):
    _entity = Event
