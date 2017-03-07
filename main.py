from __future__ import absolute_import

import tornado.ioloop
import tornado.web

from app import config
from app.handlers.database import DatabaseHandler
from app.handlers.async_fetch import AsyncFetchHandler
from app.handlers.main import MainHandler
from app.handlers.json_api import JsonApiHandler


def make_application():
    settings = config.get('tornado')
    _app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/json_api", JsonApiHandler),
        (r"/db", DatabaseHandler),
        (r"/async_fetch", AsyncFetchHandler),
    ], **settings)
    return _app

if __name__ == "__main__":
    application = make_application()
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
