from sqlalchemy import CHAR, Column, DateTime, Integer, String

from .base import Model


class Item(Model):
    __tablename__ = 'item'
    attrs = [
        'uuid',
        'name',
        'value',
        'created_at',
    ]

    uuid = Column(CHAR(36), primary_key=True)
    name = Column(String(100), nullable=False)
    value = Column(Integer)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, index=True, nullable=False)
    deleted_at = Column(DateTime, index=True)
