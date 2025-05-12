#IMPORT COMUM
import pytest

#

#IMPORT PRÁTICO
from src.app.entities.user import User

from src.app.repo.user_repository_mock import UserRepositoryMock

class Test_UserRepositoryMock:

    def test_create_user(self):
        repo = UserRepositoryMock()
        len_before = len(repo.users)
        user = User(name="test", agency="0000", account="00000-0", current_balance=0.0)
        repo.create_user(user)
        len_after = len(repo.users)
        assert len_after == len_before + 1
        assert repo.users.get(1) == user

    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_user(user_id=1)
        assert user == repo.users.get(1)
