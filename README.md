# XRWVM Fullstack Developer Capstone Project

A comprehensive dealership management and review platform built as part of the IBM Full Stack Developer Professional Certificate. This project integrates a Django backend, a React frontend, and multiple microservices for database management and sentiment analysis.

## 🏗️ Architecture Overview

The application follows a microservices-based architecture:

- **Frontend**: React.js SPA (served as a production build through Django).
- **Backend**: Django (handles user authentication, car inventory, and routing).
- **Database Proxy**: Node.js Express API (manages dealer and review data via Mongoose).
- **Database**: MongoDB (In-memory mock used for simplified portable local setup).
- **AI Microservice**: Flask (provides sentiment analysis using NLTK VADER).

## 🚀 Tech Stack

- **Languages**: Python 3.14+, JavaScript (Node.js 22+)
- **Backend**: Django 6.0, Gunicorn
- **Frontend**: React 18, Bootstrap
- **Microservices**: Express.js, Flask
- **Database**: MongoDB (Mongoose)
- **AI/ML**: NLTK (Sentiment Analysis)

## 🛠️ Service Breakdown

| Service | Port | Description |
| :--- | :--- | :--- |
| **Django App** | `8000` | Main application hub & user portal. |
| **Node API** | `3030` | Management service for dealership data. |
| **Sentiment API** | `5050` | NLP service for review sentiment profiling. |

## ⚙️ Local Setup & Running

The project environment is pre-configured with a local Python virtual environment (`venv2`).

### 1. Start Database Proxy (Node.js)
```bash
cd server/database
npm install
node app.js
```

### 2. Start Sentiment Analyzer (Flask)
```bash
cd server/djangoapp/microservices
flask run --port=5050
```

### 3. Start Main Application (Django)
```bash
cd server
source venv2/bin/activate
python manage.py runserver 0.0.0.0:8000
```

Access the application at: **[http://localhost:8000](http://localhost:8000)**

## ✅ Project Completion Status
This repository has been fully audited and initialized. All **28/28** Capstone Tasks have been completed, verified via automated browser testing, and documented in the `solved_tasks/` directory.

---
*Developed as part of the IBM Full Stack Developer Capstone.*