# from unittest import TestCase
from tornado.testing import AsyncTestCase, gen_test

from app.services.event import EventService
from app.services.repositories.event import EventRepository


class TestEventService(AsyncTestCase):

    @gen_test
    def test_create_event(self):
        event = yield EventService.create(
            name='123',
            latitude=12.2323,
            longitude=45.3434,
            created_by='ef29db3c-7914-4af1-a9c4-063a0eb77778',
        )
        obj = EventRepository.read_one(event.uuid)
        assert obj
