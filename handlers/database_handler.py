from __future__ import absolute_import

from tornado import gen
from tornado import httpclient
from tornado.web import RequestHandler


class DatabaseHandler(RequestHandler):

    def initialize(self, db):
        self.db = db
        print db

    @gen.coroutine
    def get(self):
        self.write(self.db)
