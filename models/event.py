from sqlalchemy import CHAR, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Model, CreatedUpdatedDeletedTimestamp


class Event(Model, CreatedUpdatedDeletedTimestamp):

    __tablename__ = 'event'

    attrs = [
        'uuid',
        'name',
        'latitude',
        'longitude',
        'created_by',
        'created_at',
        'updated_at',
        'deleted_at',
    ]

    uuid = Column(CHAR(36), primary_key=True)
    name = Column(String(100), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    created_by = Column(CHAR(36), ForeignKey('user.uuid'), nullable=False)

    user = relationship("User")
