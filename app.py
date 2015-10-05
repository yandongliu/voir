from __future__ import absolute_import

import tornado.ioloop
import tornado.web

from handlers.error_handler import ErrorHandler
from handlers.database_handler import DatabaseHandler
from handlers.fetch_handler import FetchHandler
from handlers.main_handler import MainHandler
from handlers.message_handler import MessageHandler

db = None

def init_db():
    global db
    db = 'abc'

def make_application():
    settings = {
        'default_handler_class': ErrorHandler,
        'template_path': 'templates/',
    }
    _app =  tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/messages", MessageHandler),
        (r"/api/db", DatabaseHandler, dict(db=db)),
        (r"/async_fetch", FetchHandler),
    ], **settings)
    return _app

if __name__ == "__main__":
    init_db()
    application = make_application()
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
