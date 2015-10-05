from __future__ import absolute_import

from .base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
