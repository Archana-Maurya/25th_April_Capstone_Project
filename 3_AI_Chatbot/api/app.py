from fastapi import FastAPI
import joblib

app = FastAPI()

# Load chatbot data
df = joblib.load("../models/chatbot_data.pkl")


@app.get("/")
def home():
    return {
        "project": "Intelligent Customer Support Chatbot",
        "student_name": "Archana Maurya",
        "message": "Chatbot API Running Successfully"
    }


@app.post("/chat")
def chat(query: str):
    query = query.lower()

    for index, row in df.iterrows():
        if query == row["Query"]:
            return {
                "response": row["Response"]
            }

    return {
        "response": "Sorry, I could not understand your query. Please contact support."
    }