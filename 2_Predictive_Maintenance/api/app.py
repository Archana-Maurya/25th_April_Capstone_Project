from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load trained model
model = joblib.load("../models/failure_model.pkl")


@app.get("/")
def home():
    return {
        "project": "Predictive Maintenance System",
        "student_name": "Archana Maurya",
        "message": "API Running Successfully"
    }


@app.post("/predict-failure")
def predict_failure(
    MachineID: int,
    Temperature: float,
    Vibration: float,
    Pressure: float,
    Humidity: float,
    Year: int,
    Month: int,
    Day: int,
    Hour: int,
    Minute: int
):
    input_data = pd.DataFrame([[
        MachineID,
        Temperature,
        Vibration,
        Pressure,
        Humidity,
        Year,
        Month,
        Day,
        Hour,
        Minute
    ]], columns=[
        "MachineID",
        "Temperature",
        "Vibration",
        "Pressure",
        "Humidity",
        "Year",
        "Month",
        "Day",
        "Hour",
        "Minute"
    ])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    return {
        "Failure_Prediction": int(prediction[0]),
        "Failure_Probability": round(float(max(probability[0])), 2)
    }