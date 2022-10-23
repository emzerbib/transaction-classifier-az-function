import logging
import azure.functions as func
import pickle
import warnings 
from HttpTriggerTest.utils.models import TransactionInput
from HttpTriggerTest.utils.classification import convert_input_to_array

CLASSIFIER_PATH = "HttpTriggerTest/utils/transformers/classifier.sav"
VECTORIZER_PATH = "HttpTriggerTest/utils/transformers/word_vectorizer.sav"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    loaded_model = pickle.load(open(CLASSIFIER_PATH, 'rb'))
    loaded_vectorizer = pickle.load(open(VECTORIZER_PATH, 'rb'))


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    takes a TransactionInput object with parameters (amount, hour and tag) 
    and returns a transaction type (client, supplier or tax)
    """
    logging.info('Python HTTP trigger function processed a request.')
    parameters = {
        "amount" : req.params.get('amount'),
        "hour" : req.params.get('hour'),
        "tag" : req.params.get('tag')
        }

    input_transaction = TransactionInput(**parameters)
    input_array = convert_input_to_array(input_transaction)
    prediction = loaded_model.predict(input_array)
    
    return func.HttpResponse(f"The prediction is a: {prediction}")




