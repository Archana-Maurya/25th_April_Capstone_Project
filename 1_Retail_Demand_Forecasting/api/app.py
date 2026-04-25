from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("../models/demand_model.pkl")

@app.get("/")
def home():
    return {
        "message": "Smart Retail Demand Forecasting API Running Successfully"
    }

@app.post("/predict-demand")
def predict_demand(
    ProductID: int,
    Category: int,
    Region: int,
    Price: float,
    Discount: float,
    Holiday: int,
    Year: int,
    Month: int,
    Day: int
):
    input_data = pd.DataFrame([[
        ProductID,
        Category,
        Region,
        Price,
        Discount,
        Holiday,
        Year,
        Month,
        Day
    ]], columns=[
        "ProductID",
        "Category",
        "Region",
        "Price",
        "Discount",
        "Holiday",
        "Year",
        "Month",
        "Day"
    ])

    prediction = model.predict(input_data)

    return {
        "Predicted_Demand": round(float(prediction[0]), 2)
    }