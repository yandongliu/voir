from mappers.user import UserMapper
from models import User
from services.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    Table = User.__table__
    Mapper = UserMapper
