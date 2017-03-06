from datetime import datetime

from schematics.models import Model
from schematics.types import DateTimeType, IntType, StringType

from .base import TimestampModel, UuidStringType


class Item(TimestampModel):

    uuid = UuidStringType(required=True)
    name = StringType(required=True)
    value = IntType()
    user_uuid = StringType(required=True)
