from datetime import datetime

from schematics.models import Model
from schematics.types import DateTimeType, IntType, StringType

from .base import UuidStringType

class Item(Model):

    uuid = UuidStringType(required=True)
    name = StringType(required=True)
    value = IntType()
    created_at = DateTimeType(default=datetime.utcnow, required=True)
    updated_at = DateTimeType(default=datetime.utcnow, required=True)
    deleted_at = DateTimeType(default=datetime.utcnow)
