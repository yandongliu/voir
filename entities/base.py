import uuid

from schematics.exceptions import ValidationError
from schematics.types import StringType


class UuidStringType(StringType):
    def validate1(self, value, field_context=None):
        try:
            uuid.UUID(value, version=4)
        except ValueError:
            raise ValidationError('Value should be valid UUID, got \'%s\' instead' % value)

    def _mock(self, context=None):
        return str(uuid.uuid4())
