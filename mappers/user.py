from __future__ import absolute_import

from entities.user import User
from .base import EntityMapper


class UserMapper(EntityMapper):
    _entity = User

