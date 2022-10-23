from HttpTriggerTest.utils.columns import Columns
from HttpTriggerTest.utils.models import TransactionInput, TransactionType
import random, json

with open("HttpTriggerTest/utils/reference/transaction_param.json") as json_file:
    PARAMETER_DICT = json.load(json_file)

def generate_transactionInput(transaction_type: TransactionType) -> TransactionInput:
    """returns a TransactionInput object of type transaction_type with random features"""
    parameters = {
        Columns.AMOUNT : random.randint(*PARAMETER_DICT[transaction_type][Columns.AMOUNT_RANGE]),
        Columns.TAG : random.choice(PARAMETER_DICT[transaction_type][Columns.TAG_CHOICES]),
        Columns.HOUR : random.randint(*PARAMETER_DICT[transaction_type][Columns.HOUR_RANGE])
        }

    return TransactionInput(**parameters)