from schematics.types import IntType, StringType

from .base import TimestampModel, UuidStringType


class Item(TimestampModel):

    uuid = UuidStringType(required=True)
    name = StringType(required=True)
    value = IntType()
    user_uuid = StringType(required=True)
