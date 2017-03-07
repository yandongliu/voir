from datetime import datetime
from uuid import uuid4

from app.entities import Event
from app.services.repositories.user import UserRepository


class UserService(object):

    @classmethod
    def get_recent_users(cls, n=10):
        users = UserRepository.read_recent_users(n)
        return users
