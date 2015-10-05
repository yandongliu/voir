from sqlalchemy import Column, Integer, String
from sqlalchemy.types import CHAR

from models.base import Base

class Item(Base):

    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(36), nullable=True, index=True)

    def __init__(self):
        pass
