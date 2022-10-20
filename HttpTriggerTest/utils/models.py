from HttpTriggerTest.utils.columns import Columns
from pydantic import BaseModel
from enum import Enum

class TransactionInput(BaseModel):
    amount: int
    hour: int
    tag: str

class TransactionType(Enum):
    client = Columns.CLIENT 
    supplier = Columns.SUPPLIER 
    tax = Columns.TAX 