from sqlalchemy import CHAR, Column, DateTime, Integer, String

from .base import Base


class Item(Base):
        __tablename__ = 'item'

        uuid = Column(CHAR(36), primary_key=True)
        name = Column(String(100), nullable=False)
        value = Column(Integer)
        created_at = Column(DateTime, nullable=False)
        updated_at = Column(DateTime, index=True, nullable=False)
        deleted_at = Column(DateTime, index=True)

        def __repr__(self):
                return "<Item(%s, %s, %s)>" % (self.uuid, self.name, self.value)
