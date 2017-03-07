from app.mappers.user import UserMapper
from app.models.base import session
from app.models import User
from app.services.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    Table = User.__table__
    Mapper = UserMapper

    @classmethod
    def read_recent_users(cls, limit=None):
        query = cls.Table.select().order_by(
            cls.Table.c.created_at.desc()
        )
        if limit:
            query = query.limit(limit)
        rows = session.execute(query)
        if rows:
            entities = map(cls.Mapper.to_entity_from_obj, list(rows))
            return entities
