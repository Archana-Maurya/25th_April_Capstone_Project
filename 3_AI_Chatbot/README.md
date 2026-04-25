# Intelligent Customer Support Chatbot

## Student Details

**Name:** Archana Maurya  
**Course:** B.Tech – Computer Science Engineering  
**University:** Galgotias University  
**Year:** 3rd Year  
**Super Set id:** 6430994
---

## Project Overview

This project automates customer support using an AI-powered chatbot integrated with enterprise systems.

The chatbot can:

- Understand customer queries
- Provide context-aware responses
- Fetch customer details from CRM system
- Raise support tickets when required

This project includes:

- FastAPI REST API
- CRM Mock Integration
- Ticketing System
- Azure AI Foundry Deployment Concept
- Intelligent Response Generation

---

## Dataset Used

Dataset Name:

customer_support_data.csv

Columns:

- Query
- Intent
- Response

Used for:

- Query understanding
- Intent matching
- Response generation

---

## Technologies Used

- Python
- Pandas
- FastAPI
- Uvicorn
- Joblib
- Azure AI Foundry Concept

---

## API Endpoint

### Home Endpoint

GET /

Response:

{
  "message": "Chatbot API Running Successfully"
}

---

### Chat Endpoint

POST /chat

Input:

{
  "query": "Where is my order?"
}

Sample Output:

{
  "response": "Your order is on the way."
}

---

## CRM Integration (Mock)

The chatbot fetches customer details such as:

- Customer Name
- Order Status
- Previous Support Tickets

Example:

{
  "customer_name": "Archana Maurya",
  "order_status": "Your order is on the way",
  "previous_ticket": "No previous tickets found"
}

---

## Ticket System (Mock)

If chatbot cannot understand a query:

- Support ticket is created automatically

Example:

{
  "ticket_id": "T101",
  "status": "Ticket Created Successfully",
  "issue": "Order delayed"
}

---

## Azure Deployment Endpoint (Demo)

https://customer-support-chatbot.azurewebsites.net/chat

---

## Architecture Design

Flow:

User → Chatbot → API → CRM → Ticket System

---

## Project Structure

3_AI_Chatbot/

- dataset/
- notebook/
- models/
- api/
- backend/
- prompts/
- architecture/
- screenshots/
- README.md
- requirements.txt

---

## Conclusion

This project successfully demonstrates enterprise chatbot automation using FastAPI, backend integration, and deployment-ready architecture.