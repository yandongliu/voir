from mappers.user import UserMapper
from models.base import session
from models import User
from services.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    Table = User.__table__
    Mapper = UserMapper
