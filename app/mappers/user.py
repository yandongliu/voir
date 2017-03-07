from __future__ import absolute_import

from app.entities.user import User
from app.mappers.base import EntityMapper


class UserMapper(EntityMapper):
    _entity = User
