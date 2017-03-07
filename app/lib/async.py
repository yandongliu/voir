from tornado import gen
from tornado.concurrent import run_on_executor, futures
from tornado.ioloop import IOLoop


class TaskRunner(object):
    def __init__(self, loop=None):
        self.executor = futures.ThreadPoolExecutor(4)
        self.loop = loop or IOLoop.instance()

    @run_on_executor
    def long_running_task(self, func, *args, **kwargs):
        print 'running task', func, args, kwargs
        return func(*args, **kwargs)

    def async(self, func):
        @gen.coroutine
        def make_async(*args, **kwargs):
            ret = yield self.long_running_task(func, *args, **kwargs)
            raise gen.Return(ret)
        return make_async

runner = TaskRunner()
