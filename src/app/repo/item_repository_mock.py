# IMPORT EM COMUM
from typing import Dict, Optional, List

#IMPORT EXEMPLO
from ..enums.item_type_enum import ItemTypeEnum
from ..entities.item import Item
from .item_repository_interface import IItemRepository

#IMPORT PRÁTICO
from ..enums.item_type_enum import TransactionTypeEnum
from ..entities.item import User, Transaction
from .item_repository_interface import UserRepository, TransactionRepository
import time

#CLASS EXEMPLO
class ItemRepositoryMock(IItemRepository):
    items: Dict[int, Item]
    
    def __init__(self):
        self.items = {
            1: Item(name="Barbie", price=48.90, item_type=ItemTypeEnum.TOY, admin_permission=False),
            2: Item(name="Hamburguer", price=38.00, item_type=ItemTypeEnum.FOOD, admin_permission=False),
            3: Item(name="T-shirt", price=22.95, item_type=ItemTypeEnum.CLOTHES, admin_permission=False),
            4: Item(name="Super Mario Bros", price=55.00, item_type=ItemTypeEnum.GAMES, admin_permission=True)
        }
        
    def get_all_items(self) -> List[Item]:
        return self.items.values()
    
    def get_item(self, item_id: int) -> Optional[Item]:
        return self.items.get(item_id, None)
    
    def create_item(self, item: Item, item_id: int) -> Item:
        
        self.items[item_id] = item
        return item
    
    def delete_item(self, item_id: int) -> Item:
        item = self.items.pop(item_id, None)
        return item
        
        
    def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
        item = self.items.get(item_id, None)
        if item is None:
            return None
        
        if name is not None:
            item.name = name
        if price is not None:
            item.price = price
        if item_type is not None:
            item.item_type = item_type
        if admin_permission is not None:
            item.admin_permission = admin_permission
        self.items[item_id] = item
        
        return item
        
#CLASSES PRÁTICAS

# CLASS USER
class UserRepositoryMock(UserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {}

    def create_user(self, user: User) -> User:
        user_id = len(self.users) + 1
        self.users[user_id] = user
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)
    

# CLASS TRANSACTION
class TransactionRepositoryMock(TransactionRepository):

    all_transactions: List[Transaction]

    def __init__(self, user_repo: UserRepositoryMock):
        self.user_repo = user_repo
        self.all_transactions = []


    def update_current_balance(self, user_id: int, transaction_type: TransactionTypeEnum, value: float) -> dict:
        user = self.user_repo.get_user(user_id)
        if user is None:
            raise ValueError("Usuário não encontrado")

        start = time.time()

        if transaction_type == TransactionTypeEnum.DEPOSIT:
            user.current_balance += value
        elif transaction_type == TransactionTypeEnum.WITHDRAW:
            if user.current_balance < value:
                raise ValueError("Saldo insuficiente")
            user.current_balance -= value

        end = time.time()
        execution_time_ms = (end - start) * 1000

        transaction = Transaction(
        current_balance=user.current_balance,
        timestamp=execution_time_ms,
        Transaction_type=transaction_type.value,
        value=value
        )

        self.all_transactions.append(transaction)
        return {"current_balance": user.current_balance, "timestamp": execution_time_ms}
    
    def get_transactions(self) -> List[dict]:
        return [tx.to_dict() for tx in self.all_transactions]