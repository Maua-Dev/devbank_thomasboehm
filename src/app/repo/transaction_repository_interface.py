from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.transaction import Transaction




class TransactionRepository(ABC):
    @abstractmethod
    def update_current_balance(self, current_balance: float, transaction_type: str, value: float) -> dict[float, float]:
        '''
        Updates the current balance of the user;
        adds the transaction to the transaction records;
        returns the new balance and the execution time in milliseconds.
        '''
        pass
    @abstractmethod
    def get_transactions(self) -> List[dict]:
        '''
        Returns a list of all transaction records
        '''
        pass