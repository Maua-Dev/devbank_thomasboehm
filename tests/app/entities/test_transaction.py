
from src.app.entities.transaction import Transaction
from src.app.enums.item_type_enum import TransactionTypeEnum




 
class Test_Transaction:
    def test_validate_current_balance(self):
        assert Transaction.validate_current_balance(100.0) == (True, "")
        assert Transaction.validate_current_balance(None) == (False, "Current balance is required")
        assert Transaction.validate_current_balance("100.0") == (False, "Current balance must be a float")
        assert Transaction.validate_current_balance(-100.0) == (False, "Current balance must be a positive number")
    
    def test_validate_timestamp(self):
        assert Transaction.validate_timestamp(1633072800.0) == (True, "")
        assert Transaction.validate_timestamp(None) == (False, "Timestamp is required")
        assert Transaction.validate_timestamp("1633072800.0") == (False, "Timestamp must be a float")
    
    def test_validate_Transaction_type(self):
        assert Transaction.validate_Transaction_type("WITHDRAW") == (True, "")
        assert Transaction.validate_Transaction_type("DEPOSIT") == (True, "")
        assert Transaction.validate_Transaction_type(None) == (False, "Type is required")
        assert Transaction.validate_Transaction_type("transfer") == (False, "Type must be 'WITHDRAW' or 'DEPOSIT'")
        assert Transaction.validate_Transaction_type(123) == (False, "Type must be a string")
    
    def test_validate_value(self):
        assert Transaction.validate_value(100.0) == (True, "")
        assert Transaction.validate_value(None) == (False, "Value is required")
        assert Transaction.validate_value("100.0") == (False, "Value must be a float")
        assert Transaction.validate_value(-100.0) == (False, "Value must be a positive number")
    
    def test_to_dict(self):
        transaction = Transaction(100.0, 1633072800.0, TransactionTypeEnum.WITHDRAW.value, 50.0)
        assert transaction.to_dict() == {
            'current_balance': 100.0,
            'timestamp': 1633072800.0,
            'Transaction_type': TransactionTypeEnum.WITHDRAW.value,
            'value': 50.0
        }