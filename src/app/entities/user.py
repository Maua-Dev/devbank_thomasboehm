from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

class User:
    name: str
    agency: str
    account: str
    current_balance: float
    

    def __init__ (self, name: str=None, agency: str=None, account: str=None, current_balance: float=None):
        validate_name = self.validate_name(name)
        if validate_name[0] is False:
            raise ParamNotValidated(name, validate_name[1])
        self.name = name

        validate_agency = self.validate_agency(agency)
        if validate_agency[0] is False:
            raise ParamNotValidated(agency, validate_agency[1])
        self.agency = agency

        validate_account = self.validate_account(account)
        if validate_account[0] is False:
            raise ParamNotValidated(account, validate_account[1])
        self.account = account

        validate_current_balance = self.validate_current_balance(current_balance)
        if validate_current_balance[0] is False:
            raise ParamNotValidated(current_balance, validate_current_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False,"Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True,"")
    
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agency number is required")
        if type(agency) != str:
            return (False, "Agency number must be a string")
        if len(agency) != 4:
            return(False, "Agency number was entered incorrectly")
        return(True,"")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "Account number is required")
        if type(account) != str:
            return (False, "Account number must be a string")
        if len(account) < 6:
            return(False, "Account number was entered incorrectly")
        return(True,"")        

    @staticmethod    
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be a positive number")
        return (True, "")  

    
    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance,
        }

    def __eq__(self,other):
        return self.name == other.name and self.agency == other.agency and self.account == other.account and self.current_balance == other.current_balance
    
    def __repr__(self):
        return f"User(name={self.name}, agency={self.agency}, account={self.account}, current_balance={self.current_balance})"

