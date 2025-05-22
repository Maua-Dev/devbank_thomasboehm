from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.main import get_user, get_history, deposit, withdraw, create_user
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock

class Test_Main:
    def test_get_history(self):
        repo = TransactionRepositoryMock()
        response = get_history()
        assert all([item_expect.to_dict() == item for item_expect, item in zip(repo.all_transactions, response)])
        assert len(response) == len(repo.all_transactions)

    def test_get_user(self):
        repo = UserRepositoryMock()
        user_id = 1
        response = get_user(user_id=user_id)
        assert response == {
            'user_id' : user_id,
            'user': repo.user.get(user_id).to_dict()
        }
        
    def test_get_user_id_is_none(self):

        user_id = None
        with pytest.raises(HTTPException) as err:
            get_user(user_id=user_id)

    def test_deposit(self):
        repo = UserRepositoryMock()
        user_id = 1
        request = {
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        }
        response = deposit(user_id=user_id, request=request)
        assert response == {
            'current_balance': repo.user.get(user_id).current_balance,
            'timestamp': response['timestamp']
        }
    
    def test_deposit_suspeito(self):
        repo = UserRepositoryMock()
        user_id = 1
        request = {
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        }
        with pytest.raises(HTTPException) as err:
            deposit(user_id=user_id, request=request)
        
    def test_withdraw(self):
        repo = UserRepositoryMock()
        user_id = 1
        request = {
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        }
        response = withdraw(user_id=user_id, request=request)
        assert response == {
            'current_balance': repo.user.get(user_id).current_balance,
            'timestamp': response['timestamp']
        }

    def test_not_enough_balance(self):
        repo = UserRepositoryMock()
        user_id = 1
        request = {
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        }
        with pytest.raises(HTTPException) as err:
            withdraw(user_id=user_id, request=request)
    
    def test_create_user(self):
        repo = UserRepositoryMock()
        user_id = 1
        request = {
            "name": "John Doe",
            "agency": "001",
            "account_number": "123456",
            "current_balance": 0.0
        }
        response = create_user(user_id=user_id, request=request)
        assert response == {
            "user_id": user_id,
            "user": repo.user.get(user_id).to_dict()
        }