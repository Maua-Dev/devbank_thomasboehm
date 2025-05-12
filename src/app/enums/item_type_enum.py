from enum import Enum

class ItemTypeEnum(Enum):
    TOY="TOY"
    FOOD="FOOD"
    CLOTHES="CLOTHES"
    GAMES="GAMES"

class TransactionTypeEnum(Enum):
    DEPOSIT="DEPOSIT"
    WITHDRAW="WITHDRAW"