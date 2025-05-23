#IMPORT COMUM
import pytest


#IMPORT PRÁTICO
from src.app.entities.user import User
from src.app.entities.transaction import Transaction
from src.app.enums.item_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.repo.user_repository_mock import UserRepositoryMock


class Test_TransactionRepositoryMock:
    def test_update_current_balance(self):
        user_repo = UserRepositoryMock()
        user = User(name="test", agency="0000", account="00000-0", current_balance=0.0)
        user_repo.create_user(user)
        
        transaction_repo = TransactionRepositoryMock(user_repo=user_repo)
        transaction_type = TransactionTypeEnum.DEPOSIT
        value = 100.0
        
        result = transaction_repo.update_current_balance(user_id=1, transaction_type=transaction_type, value=value)
        
        assert result["current_balance"] == 100.0
        assert len(transaction_repo.all_transactions) == 1
        assert transaction_repo.all_transactions[0].Transaction_type == transaction_type.value
   
    def test_get_transactions(self):
        user_repo = UserRepositoryMock()
        user = User(name="test", agency="0000", account="00000-0", current_balance=0.0)
        user_repo.create_user(user)
        
        transaction_repo = TransactionRepositoryMock(user_repo=user_repo)
        transaction_type = TransactionTypeEnum.DEPOSIT
        value = 100.0
        
        transaction_repo.update_current_balance(user_id=1, transaction_type=transaction_type, value=value)
        
        transactions = transaction_repo.get_transactions()

        assert len(transactions) == 1
        assert transactions[0]["current_balance"] == 100.0
        assert transactions[0]["Transaction_type"] == transaction_type.value
        assert transactions[0]["value"] == value
        assert transactions[0]["timestamp"] > 0

    def test_update_current_balance_user_not_found(self):
        user_repo = UserRepositoryMock()
        transaction_repo = TransactionRepositoryMock(user_repo=user_repo)
        transaction_type = TransactionTypeEnum.DEPOSIT
        value = 100.0
        in_use_user_id = 999
        # Simulate a user not found scenario
        result = transaction_repo.update_current_balance(user_id=in_use_user_id, transaction_type=transaction_type, value=value)
        
        assert result is None
    
