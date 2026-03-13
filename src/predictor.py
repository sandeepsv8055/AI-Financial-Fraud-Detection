from src.pipeline import pipeline
from src.alerts import fraud_alert


def predict(data):

    result, score = pipeline(data)

    if result == "fraud":

        fraud_alert(data)

    return result, score