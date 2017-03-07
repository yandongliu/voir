from unittest import TestCase

from app.entities import User
from app.services.repositories.user import UserRepository


class TestUserRepository(TestCase):

    def test_write_one(self):
        # import pdb; pdb.set_trace()
        user = User.get_mock_object()
        UserRepository.write_one(user)
        obj = UserRepository.read_one(user.uuid)
        assert obj.uuid == user.uuid
        assert obj.email == user.email
