from HttpTriggerTest.utils.columns import Columns
from pydantic import BaseModel
from enum import Enum

class TransactionInput(BaseModel):
    """standard input for the transaction classifier API"""
    amount: int
    hour: int
    tag: str

class TransactionType(Enum):
    """
    transaction type determines feature range/choices when instantiating a TransactionInput
    via a random generator function
    """
    client = Columns.CLIENT 
    supplier = Columns.SUPPLIER 
    tax = Columns.TAX 