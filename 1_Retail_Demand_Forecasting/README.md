# Smart Retail Demand Forecasting System

## Student Details

**Name:** Archana Maurya  
**Course:** B.Tech – Computer Science Engineering  
**University:** Galgotias University  
**Year:** 3rd Year  
**Super Set id:** 6430994
---

## Project Overview

This project predicts product demand for a retail company to help optimize inventory management and avoid overstocking or stockouts.

The system uses Machine Learning (Regression Model) to forecast future product demand based on:

- Product ID
- Category
- Region
- Price
- Discount
- Holiday
- Date Information

This project includes:

- FastAPI REST API
- MLflow Model Versioning
- Data Drift Detection
- Azure Deployment Endpoint (Demo)
- Model Monitoring Concept

---

## Dataset Used

Dataset Name:

retail_sales_data.csv

Columns:

- Date
- ProductID
- Category
- Region
- Price
- Discount
- Holiday
- UnitsSold

Target Column:

UnitsSold

Used for:

Future demand prediction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- MLflow
- Joblib
- Azure Deployment Concept

---

## Model Used

Random Forest Regressor

Evaluation Metrics:

- MAE = 47.21
- RMSE = 54.81

These metrics help evaluate model prediction accuracy.

---

## API Endpoint

### Home Endpoint

GET /

Response:

{
  "message": "Smart Retail Demand Forecasting API Running Successfully"
}

---

### Prediction Endpoint

POST /predict-demand

Input Parameters:

{
  "ProductID": 1,
  "Category": 1,
  "Region": 1,
  "Price": 25000,
  "Discount": 10,
  "Holiday": 0,
  "Year": 2024,
  "Month": 4,
  "Day": 25
}

Sample Output:

{
  "Predicted_Demand": 138.42
}

---

## MLflow Tracking

Used for:

- Model Versioning
- Experiment Tracking
- Performance Monitoring

Example:

- Version 1 → Random Forest
- Version 2 → Improved Model

MLflow Dashboard URL:

http://127.0.0.1:5000

---

## Data Drift Detection

Used for:

- Seasonal demand changes detection
- Sudden sales pattern monitoring

Example:

Festival season demand spike detection

This helps improve retraining decisions.

---

## Azure Deployment Endpoint (Demo)

https://retail-demand-api.azurewebsites.net/predict-demand

This represents deployment-ready cloud architecture using Azure.

---

## Project Structure

1_Retail_Demand_Forecasting/

- dataset/
- notebook/
- models/
- api/
- mlflow/
- drift_detection/
- screenshots/
- README.md
- requirements.txt

---

## Conclusion

This project successfully demonstrates an end-to-end MLOps workflow including:

- Data preprocessing
- Model training
- Evaluation
- Deployment
- API integration
- Monitoring
- Version control

It provides a production-ready demand forecasting solution for smart retail systems.