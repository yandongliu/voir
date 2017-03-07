from __future__ import absolute_import

from app.handlers.base import BaseHandler
from app.lib import util


class JsonApiHandler(BaseHandler):
    def get(self):
        result = []
        for i in xrange(10):
            result.append({'number': i, 'value': util.random_string()})
        self.json_response(result)
