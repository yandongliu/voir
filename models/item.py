from sqlalchemy import CHAR, Column, DateTime, Integer, String

from .base import Base

class Item(Base):
        __tablename__ = 'item'

        uuid = Column(CHAR(36), primary_key=True)
        name = Column(String(100), nullable=False)
        value = Column(Integer)
        created_at = Column('created_at', DateTime, nullable=False)
        updated_at = Column('updated_at', DateTime, index=True, nullable=False)
        deleted_at = Column('deleted_at', DateTime, index=True)

        def __init2__(self, uuid, name, value):
                self.uuid = uuid
                self.name = name
                self.value = value

        def __repr__(self):
                return "<Item(%s, %s, %s)>" % (self.uuid, self.name, self.value)
