from __future__ import absolute_import

from tornado import gen
from tornado.web import RequestHandler

from models.base import session
from models.item import Item


class DatabaseHandler(RequestHandler):

    @gen.coroutine
    def get(self):
        all_records = session.query(Item).all()
        self.write({'data': [str(r) for r in all_records]})
