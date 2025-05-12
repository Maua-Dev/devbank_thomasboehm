from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

#CLASS EXAMPLE

class Item:
    name: str
    price: float
    item_type: ItemTypeEnum
    admin_permission: bool = False
    
    def __init__(self, name: str=None, price: float=None, item_type: ItemTypeEnum=None, admin_permission: bool=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name
        
        validation_price = self.validate_price(price)
        if validation_price[0] is False:
            raise ParamNotValidated("price", validation_price[1])
        self.price = price

        validation_item_type = self.validate_item_type(item_type)
        if validation_item_type[0] is False:
            raise ParamNotValidated("item_type", validation_item_type[1])
        self.item_type = item_type
        
        validation_admin_permission = self.validate_admin_permission(admin_permission)
        if validation_admin_permission[0] is False:
            raise ParamNotValidated("admin_permission", validation_admin_permission[1])
        self.admin_permission = admin_permission
        
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
        
    @staticmethod
    def validate_price(price: float) -> Tuple[bool, str]:
        if price is None:
            return (False, "Price is required")
        if type(price) != float:
            return (False, "Price must be a float")
        if price < 0:
            return (False, "Price must be a positive number")
        return (True, "")
    
    @staticmethod
    def validate_item_type(item_type: ItemTypeEnum) -> Tuple[bool, str]:
        if item_type is None:
            return (False, "Item type is required")
        if type(item_type) != ItemTypeEnum:
            return (False, "Item type must be a ItemTypeEnum")
        return (True, "")
    
    @staticmethod
    def validate_admin_permission(admin_permission: bool) -> Tuple[bool, str]:
        if admin_permission is None:
            return (False, "Admin permission is required")
        if type(admin_permission) != bool:
            return (False, "Admin permission must be a boolean")
        return (True, "")
        
    @staticmethod
    def validate_item_id(item_id: int) -> Tuple[bool, str]:
        if item_id is None:
            return (False, "Missing 'item_id' parameter")

        if type(item_id) != int:
            return (False, "Parameter 'item_id' must be an integer")
        
        if item_id < 0:
            return (False, "Parameter 'item_id' must be a positive integer")

        return (True, "")
    
        
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "item_type": self.item_type.value,
            "admin_permission": self.admin_permission
        }
    
    def __eq__(self,other):
        return self.name == other.name and self.price == other.price and self.item_type == other.item_type and self.admin_permission == other.admin_permission
    
    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, item_type={self.item_type}, admin_permission={self.admin_permission})"

#CLASS USER

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




class Transaction:
        current_balance: float
        timestamp: float
        Transaction_type: str
        value: float

        def __init__ (self, current_balance: float=None, timestamp: float=None, Transaction_type: str=None, value: float=None):
            validate_current_balance = self.validate_current_balance(current_balance)
            if validate_current_balance[0] is False:
             raise ParamNotValidated(current_balance, validate_current_balance[1])
            self.current_balance = current_balance

            validate_timestamp = self.validate_timestamp(timestamp)
            if validate_timestamp[0] is False:
                raise ParamNotValidated(timestamp, validate_timestamp[1])
            self.timestamp = timestamp

            validate_Transaction_type = self.validate_Transaction_type(Transaction_type)
            if validate_Transaction_type[0] is False:
                raise ParamNotValidated(Transaction_type, validate_Transaction_type[1])
            self.Transaction_type = Transaction_type

            validate_value = self.validate_value(value)
            if validate_value[0] is False:
                raise ParamNotValidated(value, validate_value[1])
            self.value = value

        @staticmethod    
        def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
            if current_balance is None:
                return (False, "Current balance is required")
            if type(current_balance) != float:
                 return (False, "Current balance must be a float")
            if current_balance < 0:
                 return (False, "Current balance must be a positive number")
            return (True, "")  

        @staticmethod
        def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
            if timestamp is None:
                return (False, "Timestamp is required")
            if type(timestamp) != float:
                return (False, "Timestamp must be a float")
            return (True, "")  

        @staticmethod
        def validate_Transaction_type(Transaction_type: str) -> Tuple[bool, str]:
            if Transaction_type is None:
                return (False, "Type is required")
            if Transaction_type.lower() not in ["withdraw", "deposit"]:
                return (False, "Type must be 'withdraw' or 'deposit'")
            if type(Transaction_type) != str:
                return (False, "Type must be a string")
            return (True, "")
    
        @staticmethod
        def validate_value(value: float) -> Tuple[bool, str]:
            if value is None:
                return (False, "Value is required")
            if type(value) != float:
                return (False, "Value must be a float")
            if value < 0:
                return (False, "Value must be a positive number")
            return (True, "")
        
        def to_dict(self):
            return {
                "value": self.value,
                "Transaction_type": self.Transaction_type,
                "current_balance": self.current_balance,
                "timestamp": self.timestamp,
            }

        def __eq__(self, other):
            return self.current_balance == other.current_balance and self.timestamp == other.timestamp and self.Transaction_type == other.Transaction_type and self.value == other.value

        def __repr__(self):
            return f"Transaction(current_balance={self.current_balance}, timestamp={self.timestamp}, Transaction_type={self.Transaction_type}, value={self.value})"