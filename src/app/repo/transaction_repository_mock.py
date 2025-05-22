# IMPORT EM COMUM
from typing import Dict, Optional, List


#IMPORT PRÁTICO
from ..enums.item_type_enum import TransactionTypeEnum
from ..entities.transaction import Transaction
from .transaction_repository_interface import TransactionRepository
from .user_repository_mock import UserRepositoryMock
import time

class TransactionRepositoryMock(TransactionRepository):

    all_transactions: List[Transaction]

    def __init__(self, transaction_repo: UserRepositoryMock):
        self.transaction_repo = transaction_repo
        self.all_transactions = []


    def update_current_balance(self, user_id: int, transaction_type: TransactionTypeEnum, value: float) -> dict:
        user = self.transaction_repo.get_user(user_id)
        start = time.time()
        if user is None:
            return None

        
        if transaction_type == TransactionTypeEnum.DEPOSIT:
            user.current_balance += value
        elif transaction_type == TransactionTypeEnum.WITHDRAW:
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