#IMPORT COMUM
import pytest

#IMPORT EXEMPLO
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.repo.item_repository_mock import ItemRepositoryMock

#IMPORT PRÁTICO
from src.app.entities.item import User, Transaction
from src.app.enums.item_type_enum import TransactionTypeEnum
from src.app.repo.item_repository_mock import UserRepositoryMock, TransactionRepositoryMock

class Test_ItemRepositoryMock:
    def test_get_all_items(self):
        repo = ItemRepositoryMock()
        assert all([item_expect == item for item_expect, item in zip(repo.items.values(), repo.get_all_items())]) 
        
    def test_get_item(self):
        repo = ItemRepositoryMock()
        item = repo.get_item(item_id=1)
        assert item == repo.items.get(1)
    
    def test_get_item_not_found(self):
        repo = ItemRepositoryMock()
        item = repo.get_item(item_id=10)
        assert item is None
        
    def test_create_item(self):
        repo = ItemRepositoryMock()
        len_before = len(repo.items)
        item = Item(name="test", price=1.0, item_type=ItemTypeEnum.TOY, admin_permission=False)
        repo.create_item(item=item, item_id=0)
        len_after = len(repo.items)
        assert len_after == len_before + 1
        assert repo.items.get(0) == item
        
    def test_delete_item(self):
        repo = ItemRepositoryMock()
        item_expected_to_be_deleted = repo.items.get(1)
        len_before = len(repo.items)
        
        item = repo.delete_item(item_id=1)
        len_after = len(repo.items)
        assert len_after == len_before - 1
        assert item == item_expected_to_be_deleted
        
    def test_delete_item_not_found(self):
        repo = ItemRepositoryMock()
        item = repo.delete_item(item_id=10)
        assert item is None
        
    def test_update_item(self):
        repo = ItemRepositoryMock()
        item = Item(name="test", price=1.0, item_type=ItemTypeEnum.TOY, admin_permission=False)
        item_updated = repo.update_item(item_id=1, name=item.name, price=item.price, item_type=item.item_type, admin_permission=item.admin_permission)
        
        assert item_updated == item
        assert repo.items.get(1) == item
        
    def test_update_item_partial_1(self):
        repo = ItemRepositoryMock()
        name = "test"
        item_updated = repo.update_item(item_id=1, name=name)
        
        assert item_updated.name == name
        assert repo.items.get(1).name == name
        
    def test_update_item_partial_2(self):
        repo = ItemRepositoryMock()
        price = 1.0
        item_updated = repo.update_item(item_id=1, price=price)
        
        assert item_updated.price == price
        assert repo.items.get(1).price == price


class Test_TransactionRepositoryMock:


    def test_transaction_repository():
        # Setup
        user_repo = UserRepositoryMock()
        transaction_repo = TransactionRepositoryMock(user_repo)

        # Criar usuário
        user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=0.0)
        created_user = user_repo.create_user(user)

        user_id = 1  # primeiro usuário criado

        # Testar depósito
        deposit_result = transaction_repo.update_current_balance(user_id, TransactionTypeEnum.DEPOSIT, 1000.0)
        assert deposit_result["current_balance"] == 1000.0
        assert "timestamp" in deposit_result

        # Testar saque
        withdraw_result = transaction_repo.update_current_balance(user_id, TransactionTypeEnum.WITHDRAW, 200.0)
        assert withdraw_result["current_balance"] == 800.0
        assert "timestamp" in withdraw_result

        # Testar histórico
        history = transaction_repo.get_transactions()
        assert len(history) == 2

        # Verificar conteúdo do histórico
        assert history[0]["transaction_type"] == "deposit"
        assert history[0]["value"] == 1000.0
        assert history[0]["current_balance"] == 1000.0

        assert history[1]["transaction_type"] == "withdraw"
        assert history[1]["value"] == 200.0
        assert history[1]["current_balance"] == 800.0


class Test_UserRepositoryMock:
    
    @pytest.fixture
    def user_repo():
        return UserRepositoryMock()

    def test_create_user(user_repo):
        user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0)
        created_user = user_repo.create_user(user)

        assert created_user == user
        assert created_user.name == "Vitor Soller"
        assert created_user.current_balance == 1000.0

    def test_get_existing_user(user_repo):
        user = User(name="Maria", agency="1111", account="12345-6", current_balance=500.0)
        user_repo.create_user(user)
        retrieved_user = user_repo.get_user(1)  # o primeiro inserido será id 1

        assert retrieved_user is not None
        assert retrieved_user.name == "Maria"
        assert retrieved_user.account == "12345-6"

    def test_get_nonexistent_user(user_repo):
        result = user_repo.get_user(999)
        assert result is None
