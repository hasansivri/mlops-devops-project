from fastapi import FastAPI
import os
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

# Production-ready MLflow URI from environment variable
MLFLOW_TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://mlflow:5000")

model = mlflow.pyfunc.load_model(
    model_uri="models:/my-model/Production",
    tracking_uri=MLFLOW_TRACKING_URI
)

@app.get("/")
def read_root():
    return {"message": "Model API running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}