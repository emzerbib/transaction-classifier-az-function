import os 
import logging
import azure.functions as func
import pickle
import warnings 
import numpy as np
#from utils import process_tag, convert_input_to_array, make_prediction
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    #from HttpTriggerTest.utils.classification import process_tag, convert_input_to_array, make_prediction

from HttpTriggerTest.utils.models import TransactionInput, TransactionType
from HttpTriggerTest.utils.generator import generate_transactionInput

classifier_path = "HttpTriggerTest/utils/transformers/classifier.sav"
vectorizer_path = "HttpTriggerTest/utils/transformers/word_vectorizer.sav"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    loaded_model = pickle.load(open(classifier_path, 'rb'))
    loaded_vectorizer = pickle.load(open(vectorizer_path, 'rb'))

N_FEATURES = 13

def process_tag(tag: str):
    vector = loaded_vectorizer.transform([tag])
    return vector.toarray()

def convert_input_to_array(input_transaction: TransactionInput):
    input_array = np.zeros(N_FEATURES)

    input_array[0] = input_transaction.amount
    input_array[1] = input_transaction.hour
    input_array[2:] = process_tag(input_transaction.tag)

    return input_array.reshape(1,-1)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    parameters = {
        "amount" : req.params.get('amount'),
        "hour" : req.params.get('hour'),
        "tag" : req.params.get('tag')
        }

    input_transaction = TransactionInput(**parameters)
    input_array = convert_input_to_array(input_transaction)

    prediction = loaded_model.predict(input_array)
    

    #return func.HttpResponse(f"The prediction is a: {prediction.tolist()}")
    return func.HttpResponse(f"The prediction is a: {prediction}")




