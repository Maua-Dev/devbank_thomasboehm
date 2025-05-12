from typing import Tuple
from ..errors.entity_errors import ParamNotValidated



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
        def validate_Transaction_type(Transaction_type: str):
            if Transaction_type is None:
                return False, "Type is required"
            if not isinstance(Transaction_type, str):
                return False, "Type must be a string"
            if Transaction_type.upper() not in ["WITHDRAW", "DEPOSIT"]:
                return False, "Type must be 'WITHDRAW' or 'DEPOSIT'"
            return True, ""

    
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