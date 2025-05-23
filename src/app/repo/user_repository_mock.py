# IMPORT EM COMUM
from typing import Dict, Optional


#IMPORT PRÁTICO

from ..entities.user import User
from .user_repository_interface import UserRepository



class UserRepositoryMock(UserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {}

    def create_user(self, user: User) -> User:
        user_id = len(self.users) + 1
        user.id = user_id  # <-- atribui o ID ao objeto User
        self.users[user_id] = user
        return user


    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)
    

