from __future__ import absolute_import

import json
import string
from random import choice, randint

from .base import BaseHandler


def _random_string():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.whitespace
    return ''.join(choice(chars) for _ in range(randint(10, 20)))


class MessageHandler(BaseHandler):
    def get(self):
        result = []
        for i in xrange(10):
            result.append({'number': i, 'value': _random_string()})
        self.json_response(result)
