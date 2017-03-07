from unittest import TestCase

from app.entities import Event, User
from app.services.repositories.event import EventRepository
from app.services.repositories.user import UserRepository


class TestEventRepository(TestCase):

    def test_write_one(self):
        # import pdb; pdb.set_trace()
        user = User.get_mock_object()
        event = Event.get_mock_object()
        event.created_by = user.uuid
        UserRepository.write_one(user)
        EventRepository.write_one(event)
        obj = EventRepository.read_one(event.uuid)
        assert obj.uuid == event.uuid
        assert obj.created_by == user.uuid
