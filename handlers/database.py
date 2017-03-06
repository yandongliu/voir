from __future__ import absolute_import

from tornado import gen
from tornado.web import RequestHandler

from lib import cache
from services.repositories.event import EventRepository
from services.repositories.user import UserRepository


class DatabaseHandler(RequestHandler):

    @cache.local_memoize
    @gen.coroutine
    def get(self):
        events = EventRepository.read_all()
        users = UserRepository.read_all()
        self.write({
            'users': [r.to_primitive() for r in users],
            'events': [r.to_primitive() for r in events]
        })
