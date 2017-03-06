from datetime import datetime
import uuid

from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import DateTimeType, StringType


class UuidStringType(StringType):
    def validate1(self, value, field_context=None):
        try:
            uuid.UUID(value, version=4)
        except ValueError:
            raise ValidationError('Value should be valid UUID, got \'%s\' instead' % value)

    def _mock(self, context=None):
        return str(uuid.uuid4())


class TimestampModel(Model):

    created_at = DateTimeType(default=datetime.utcnow, required=True)
    updated_at = DateTimeType(default=datetime.utcnow, required=True)
    deleted_at = DateTimeType()
