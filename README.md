# Confidence-Aware Adaptive Difficulty Adjustment System

## Overview

The **Confidence-Aware Adaptive Difficulty Adjustment System** is an AIML-based intelligent adaptive platform that dynamically adjusts difficulty levels using confidence and correctness signals.

The system analyzes user performance and intelligently changes difficulty levels while maintaining stable transitions and preventing sudden difficulty oscillations.

This project demonstrates:

* Adaptive AI systems
* Intelligent decision-making
* REST API integration
* Frontend-backend communication
* Stability-controlled adaptive behavior

---

# Features

* Dynamic difficulty adjustment
* Confidence-aware AI logic
* Correctness evaluation
* REST API using FastAPI
* Frontend interface using HTML/CSS/JavaScript
* User history tracking
* Stability and smoothing logic
* Input validation
* Authentication support
* Responsive frontend UI

---

# Project Architecture

```text
Frontend Website
       ↓
REST API
       ↓
Authentication Layer
       ↓
Validation Layer
       ↓
Adaptive Decision Engine
       ↓
History Database
       ↓
Difficulty Response
```

---

# Technologies Used

## Backend

* Python
* FastAPI
* Uvicorn

## Frontend

* HTML
* CSS
* JavaScript

## Libraries

* FastAPI
* Pydantic
* Statistics
* Collections (deque)

---

# Folder Structure

```text
adaptive_system/
│
├── main.py
├── auth.py
├── validator.py
├── engine.py
├── database.py
├── models.py
├── client.html
├── requirements.txt
└── README.md
```

---

# Installation

## Step 1 — Clone Repository

```bash
git clone <repository-link>
```

OR download the project folder manually.

---

## Step 2 — Open Project Folder

```bash
cd adaptive_system
```

---

## Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Step 5 — Install Dependencies

```bash
pip install fastapi uvicorn
```

OR

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 — Start Backend Server

```bash
python -m uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## Step 2 — Start Frontend Server

Open another terminal:

```bash
python -m http.server 5500
```

Frontend runs at:

```text
http://127.0.0.1:5500/client.html
```

---

# API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## POST `/adapt`

### Request Example

```json
{
  "user_id": "U101",
  "confidence": 0.9,
  "correctness": 9
}
```

---

## Response Example

```json
{
  "user_id": "U101",
  "confidence": 0.9,
  "correctness": 9,
  "score": 0.9,
  "average_score": 0.9,
  "decision": "maintain",
  "difficulty": "medium",
  "reason": "Excellent performance"
}
```

---

# Adaptive Logic

The system uses:

* Confidence scores
* Correctness scores
* Stability control
* Rolling averages
* History tracking

Example logic:

```python
if confidence > 0.75 and correctness >= 8:
    difficulty = "hard"
```

---

# Stability Mechanism

The system prevents unstable transitions such as:

```text
easy → hard → easy
```

Using:

* streak logic
* rolling averages
* smoothing mechanisms

---

# Frontend Features

* Responsive UI
* API integration
* JSON response display
* Interactive user input form

---

# Testing

Testing methods used:

* Unit testing
* API testing
* Integration testing
* Simulation testing

---

# Challenges Solved

| Challenge               | Solution               |
| ----------------------- | ---------------------- |
| CORS errors             | Added CORSMiddleware   |
| Frontend fetch failures | Used HTTP server       |
| Difficulty oscillation  | Added stability logic  |
| Invalid inputs          | Added validation layer |

---

# Future Enhancements

* Machine Learning integration
* Reinforcement Learning
* User personalization profiles
* Database integration
* Analytics dashboard
* JWT authentication

---

# Learning Outcomes

This project provided practical experience in:

* Adaptive AI systems
* FastAPI development
* REST API design
* Frontend-backend integration
* Intelligent decision engines
* AIML-based personalization

---

# References

* FastAPI Documentation
* Python Documentation
* MDN Fetch API Documentation
* Uvicorn Documentation
