from __future__ import absolute_import

from entities.event import Event
from .base import EntityMapper


class EventMapper(EntityMapper):
    _entity = Event
