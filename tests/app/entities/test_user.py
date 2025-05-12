from src.app.entities.user import User


class Test_user:
    def test_validate_name(self):
        assert User.validate_name("test") == (True, "")
        assert User.validate_name(None) == (False, "Name is required")
        assert User.validate_name(1.0) == (False, "Name must be a string")
        assert User.validate_name("te") == (False, "Name must be at least 3 characters long")
    
    def test_validate_agency(self):
        assert User.validate_agency("1234") == (True, "")
        assert User.validate_agency(None) == (False, "Agency number is required")
        assert User.validate_agency(1234) == (False, "Agency number must be a string")
        assert User.validate_agency("123") == (False, "Agency number was entered incorrectly")
    
    def test_validate_account(self):
        assert User.validate_account("00000-0") == (True, "")
        assert User.validate_account(None) == (False, "Account number is required")
        assert User.validate_account(1234) == (False, "Account number must be a string")
    
    def test_validate_current_balance(self):
        assert User.validate_current_balance(1.0) == (True, "")
        assert User.validate_current_balance(None) == (False, "Current balance is required")
        assert User.validate_current_balance("1.0") == (False, "Current balance must be a float")
        assert User.validate_current_balance(-1.0) == (False, "Current balance must be a positive number")