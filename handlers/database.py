from __future__ import absolute_import

from tornado import gen
from tornado.web import RequestHandler

from services.repositories.item import ItemRepository


class DatabaseHandler(RequestHandler):

    @gen.coroutine
    def get(self):
        items = ItemRepository.read_all()
        self.write({'data': [r.to_primitive() for r in items]})
