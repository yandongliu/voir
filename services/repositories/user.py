from models.base import session
from models import User
from mappers.user import UserMapper


class UserRepository(object):

    UserTable = User.__table__

    @classmethod
    def read_one(cls, uuid):
        query = cls.UserTable.select().where(UserTable.c.uuid == uuid)
        rows = session.execute(query)
        if rows:
            entities = map(UserMapper.to_entity_from_obj, list(rows))
            return entities[0]

    @classmethod
    def read_all(cls):
        query = cls.UserTable.select()
        rows = session.execute(query)
        if rows:
            entities = map(UserMapper.to_entity_from_obj, list(rows))
            return entities
