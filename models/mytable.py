from sqlalchemy import Column, Integer, String

from .base import Base

class MyTable(Base):
        __tablename__ = 'mytable'

        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        value = Column(String(100))

        def __init__(self, name, value):
                self.name = name
                self.value = value

        def __repr__(self):
                return "<MyTable(%s, %s)>" % (self.name, self.value)
