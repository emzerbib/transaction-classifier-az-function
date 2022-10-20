from .columns import Columns
from .models import TransactionInput, TransactionType
import random

PARAMETER_DICT = {
        Columns.CLIENT: {
            Columns.AMOUNT_RANGE: (15, 780),
            Columns.TAG_CHOICES: ('delivery', 'bulk purchase', 'G_dist'),
            Columns.HOUR_RANGE: (10, 18)
            },
        Columns.SUPPLIER: {
            Columns.AMOUNT_RANGE: (2400, 18000),
            Columns.TAG_CHOICES: ('ABC_inc', 'XYZ_inc', 'AAA_&_BBB'),
            Columns.HOUR_RANGE: (6, 21)
            },
        Columns.TAX: {
            Columns.AMOUNT_RANGE: (900, 35000),
            Columns.TAG_CHOICES: ('CPAM', 'ARC', 'RevenuQc'),
            Columns.HOUR_RANGE: (0, 1)
            }
            }

def generate_transactionInput(transaction_type: TransactionType):

    parameters = {
        Columns.AMOUNT : random.randint(*PARAMETER_DICT[transaction_type][Columns.AMOUNT_RANGE]),
        Columns.TAG : random.choice(PARAMETER_DICT[transaction_type][Columns.TAG_CHOICES]),
        Columns.HOUR : random.randint(*PARAMETER_DICT[transaction_type][Columns.HOUR_RANGE])
        }

    return TransactionInput(**parameters)