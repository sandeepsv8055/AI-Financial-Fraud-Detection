from fastapi import FastAPI
from src.predictor import predict
from pydantic import BaseModel

app = FastAPI()


class Transaction(BaseModel):
    transaction: list


@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}


@app.post("/predict")
def fraud_detection(data: Transaction):

    result = predict(data.transaction)

    return {"prediction": result}