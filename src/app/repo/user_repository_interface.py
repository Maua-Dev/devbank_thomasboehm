from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        '''
        Returns the user with the given id.
        If the user does not exist, returns None
        '''
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        '''
        Creates a new user in the database
        '''
        pass

