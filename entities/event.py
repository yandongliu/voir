from datetime import datetime

from schematics.models import Model
from schematics.types import DateTimeType, IntType, FloatType, StringType

from .base import UuidStringType


class Event(Model):

    uuid = UuidStringType(required=True)
    name = StringType(required=True)
    latitude = FloatType(required=True)
    longitude = FloatType(required=True)
    created_by = StringType(required=True)
    created_at = DateTimeType(default=datetime.utcnow, required=True)
    updated_at = DateTimeType(default=datetime.utcnow, required=True)
    deleted_at = DateTimeType(default=datetime.utcnow)
