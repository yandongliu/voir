from datetime import datetime

from schematics.models import Model
from schematics.types import DateTimeType, IntType, FloatType, StringType

from .base import TimestampModel, UuidStringType


class Event(TimestampModel):

    uuid = UuidStringType(required=True)
    name = StringType(required=True)
    latitude = FloatType(required=True)
    longitude = FloatType(required=True)
    created_by = StringType(required=True)
