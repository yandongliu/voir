from __future__ import absolute_import

from tornado import gen
from tornado.web import RequestHandler

from app.lib import cache
from app.services.event import EventService
# from services.repositories.event import EventRepository
from app.services.repositories.user import UserRepository


class DatabaseHandler(RequestHandler):

    # @cache.local_memoize
    @gen.coroutine
    def get(self):
        events = yield EventService.read_many()
        users = UserRepository.read_many()
        self.write({
            'users': [r.to_primitive() for r in users],
            'events': [r.to_primitive() for r in events]
        })
