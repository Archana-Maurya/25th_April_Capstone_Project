# Predictive Maintenance System

## Student Details

**Name:** Archana Maurya  
**Course:** B.Tech – Computer Science Engineering  
**University:** Galgotias University  
**Year:** 4th Year  
**Super Set id:** 6430994
---

## Project Overview

This project predicts machine failure using IoT sensor data to help manufacturing companies perform maintenance before breakdown happens.

The system helps reduce:

- Downtime
- Maintenance Cost
- Unexpected Machine Failure

This project includes:

- Machine Learning Classification Model
- FastAPI REST API
- Azure ML Deployment Concept
- Failure Prediction Endpoint
- Alert System
- Monitoring Logic

---

## Dataset Used

Dataset Name:

machine_sensor_data.csv

Columns:

- Timestamp
- MachineID
- Temperature
- Vibration
- Pressure
- Humidity
- Failure

Target Column:

Failure

- 0 = No Failure
- 1 = Machine Failure

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- Azure Machine Learning Concept

---

## Model Used

Random Forest Classifier

Evaluation Result:

Accuracy = 1.0

---

## API Endpoint

### Home Endpoint

GET /

Response:

{
  "message": "Predictive Maintenance API Running Successfully"
}

---

### Prediction Endpoint

POST /predict-failure

Input Parameters:

- MachineID
- Temperature
- Vibration
- Pressure
- Humidity
- Year
- Month
- Day
- Hour
- Minute

Sample Output:

{
  "Failure_Prediction": 0,
  "Failure_Probability": 0.97
}

---

## Alert System

If machine failure is predicted:

- Maintenance Team gets alert
- Preventive maintenance starts

Example:

ALERT: Machine Failure Predicted!

---

## Azure Deployment Endpoint (Demo)

https://predictive-maintenance-api.azurewebsites.net/predict-failure

---

## Project Structure

2_Predictive_Maintenance/

- dataset/
- notebook/
- models/
- api/
- alerts/
- azure_ml/
- logs/
- screenshots/
- README.md
- requirements.txt

---

## Conclusion

This project successfully demonstrates predictive maintenance using machine learning and API integration with deployment-ready architecture.