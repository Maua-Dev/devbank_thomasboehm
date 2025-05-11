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

class user:
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
            "current_balance": self.current_balance
        }
    def __eq__(self,other):
        return self.name == other.name and self.agency == other.agency and self.account == other.account and self.current_balance == other.current_balance
    
    def __repr__(self):
        return f"Item(name={self.name}, agency={self.agency}, account={self.account}, current_balance={self.current_balance})"


#CLASS TRANSACTION

class transaction:
    qty_2: int
    qty_5: int
    qty_10: int
    qty_20: int
    qty_50: int
    qty_100: int
    qty_200: int

    def __init__(self, qty_2: int=None, qty_5: int=None, qty_10: int=None, qty_20: int=None, qty_50: int=None, qty_100: int=None, qty_200: int=None):
        validate_quantity_2 = self.validate_quantity_2(qty_2)
        if validate_quantity_2[0] is False:
            raise ParamNotValidated(qty_2,validate_quantity_2[1])
        self.qty_2 = qty_2

        validate_quantity_5 = self.validate_quantity_5(qty_5)
        if validate_quantity_5[0] is False:
            raise ParamNotValidated(qty_5,validate_quantity_5[1])

        validate_quantity_10 = self.validate_quantity_10(qty_10)
        if validate_quantity_10[0] is False:
            raise ParamNotValidated(qty_10,validate_quantity_10[1])

        validate_quantity_20 = self.validate_quantity_20(qty_20)
        if validate_quantity_20[0] is False:
            raise ParamNotValidated(qty_20,validate_quantity_20[1])

        validate_quantity_50 = self.validate_quantity_50(qty_50)
        if validate_quantity_50[0] is False:
            raise ParamNotValidated(qty_50,validate_quantity_50[1])

        validate_quantity_100 = self.validate_quantity_100(qty_100)
        if validate_quantity_100[0] is False:
            raise ParamNotValidated(qty_100,validate_quantity_100[1])

        validate_quantity_200 = self.validate_quantity_200(qty_200)
        if validate_quantity_200[0] is False:
            raise ParamNotValidated(qty_200,validate_quantity_200[1])

    @staticmethod
    def validate_quantity_2(qty_2: int) -> Tuple[bool, str]:
        if qty_2 < 0:
            return (False, "2 reais quantity must be a positive number")
        if type(qty_2) != int:
            return (False, "2 reais quantity must be an integer")
        return (True, "")

    @staticmethod
    def validate_quantity_5(qty_5: int) -> Tuple[bool, str]:
        if qty_5 < 0:
            return (False, "5 reais quantity must be a positive number")
        if type(qty_5) != int:
            return (False, "5 reais quantity must be an integer")
        return (True, "")

    @staticmethod
    def validate_quantity_10(qty_10: int) -> Tuple[bool, str]:
        if qty_10 < 0:
            return (False, "10 reais quantity must be a positive number")
        if type(qty_10) != int:
            return (False, "10 reais quantity must be an integer")
        return (True, "")

    @staticmethod
    def validate_quantity_20(qty_20: int) -> Tuple[bool, str]:
        if qty_20 < 0:
            return (False, "20 reais quantity must be a positive number")
        if type(qty_20) != int:
            return (False, "20 reais quantity must be an integer")
        return (True, "")

    @staticmethod
    def validate_quantity_50(qty_50: int) -> Tuple[bool, str]:
        if qty_50 < 0:
            return (False, "50 reais quantity must be a positive number")
        if type(qty_50) != int:
            return (False, "50 reais quantity must be an integer")
        return (True, "")

    @staticmethod
    def validate_quantity_100(qty_100: int) -> Tuple[bool, str]:
        if qty_100 < 0:
            return (False, "100 reais quantity must be a positive number")
        if type(qty_100) != int:
            return (False, "100 reais quantity must be an integer")
        return (True, "")

    @staticmethod
    def validate_quantity_200(qty_200: int) -> Tuple[bool, str]:
        if qty_200 < 0:
            return (False, "200 reais quantity must be a positive number")
        if type(qty_200) != int:
            return (False, "200 reais quantity must be an integer")
        return (True, "")

def to_dict(self):
        return {
            "2": self.qty_2,
            "5": self.qty_5,
            "10": self.qty_10,
            "20": self.qty_20,
            "50": self.qty_50,
            "100": self.qty_100,
            "200": self.qty_200
        }

def __eq__(self,other):
        return self.qty_2 == other.qty_2 and self.qty_5 == other.qty_5 and self.qty_10 == other.qty_10 and self.qty_20 == other.qty_20 and self.qty_50 == other.qty_50 and self.qty_100 == other.qty_100 and self.qty_200 == other.qty_200
def __repr__(self):
        return f"Item(2={self.qty_2}, 5={self.qty_5}, 10={self.qty_10}, 20={self.qty_20}, 50={self.qty_50}, 100={self.qty_100}, 200={self.qty_200})"

