# AI Financial Fraud Detection System

An end-to-end Machine Learning system that detects suspicious financial transactions using anomaly detection models. The project includes a real-time API and an interactive dashboard for fraud monitoring.

---

## Project Overview

Financial fraud detection is critical for banks and fintech platforms.  
This project uses **unsupervised machine learning algorithms** to detect abnormal transaction patterns.

The system analyzes transaction behavior and produces a **Fraud Risk Score** that indicates whether a transaction is normal or suspicious.

---

## Key Features

- Fraud detection using multiple ML models
- Ensemble anomaly detection
- Real-time prediction API using FastAPI
- Interactive dashboard using Streamlit
- Fraud risk score visualization
- Transaction feature analysis chart
- Alert system for suspicious transactions

---

## Machine Learning Models Used

The system uses an ensemble of anomaly detection models:

- Isolation Forest
- One-Class SVM
- DBSCAN

These models detect unusual transaction patterns and generate a fraud risk score.

---

## System Architecture

User Input
↓
Streamlit Dashboard
↓
FastAPI Prediction API
↓
ML Pipeline
(Isolation Forest + OneClassSVM + DBSCAN)
↓
Fraud Risk Score
↓
Alert System

## Project Structure
AI-Financial-Fraud-Detection
│
├── api
│ └── main.py
│
├── dashboard
│ └── app.py
│
├── models
│ ├── iso_model.pkl
│ ├── svm_model.pkl
│ ├── db_model.pkl
│ └── scaler.pkl
│
├── src
│ ├── pipeline.py
│ ├── predictor.py
│ └── alerts.py
│
├── requirements.txt
└── README.md


---

## Installation

Clone the repository:


git clone https://github.com/sandeepsv8055/AI-Financial-Fraud-Detection.git

cd AI-Financial-Fraud-Detection


Install dependencies:


pip install -r requirements.txt


---

## Running the FastAPI Server


python -m uvicorn api.main:app --reload


API will run at:


http://127.0.0.1:8000


API documentation:


http://127.0.0.1:8000/docs


---

## Running the Streamlit Dashboard


python -m streamlit run dashboard/app.py


Dashboard will open at:


http://localhost:8501


---

## Example Fraud Detection Output

Fraud Risk Score:


Risk Score: 85%
⚠ FRAUD DETECTED


Normal Transaction:


Risk Score: 32%
✅ Normal Transaction


---

## Dataset

This project uses the **Credit Card Fraud Detection Dataset**, which contains anonymized transaction features.

Features include:

- Transaction time
- Transaction amount
- PCA-transformed features (V1–V28)

---

## Technologies Used

- Python
- Scikit-learn
- FastAPI
- Streamlit
- NumPy
- Pandas
- Matplotlib

---

## Future Improvements

- Real-time fraud monitoring system
- Transaction logging database
- Email/SMS fraud alerts
- Deep learning based fraud detection
- Model performance monitoring

---

## Author

Sandeep Vishwakarma  
