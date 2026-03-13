import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.predictor import predict

st.title("AI Financial Fraud Detection System")

st.write("This dashboard detects suspicious financial transactions using AI models.")

# ------------------------------------------------
# OPTION 1 : SIMPLE USER INPUT (Normal Users)
# ------------------------------------------------

st.header("Simple Fraud Check")

amount = st.number_input("Transaction Amount", value=500.0)

# User-friendly time selection
time_options = {
    "5 sec": 5,
    "10 sec": 10,
    "30 sec": 30,
    "1 min": 60,
    "5 min": 300,
    "10 min": 600,
    "30 min": 1800,
    "1 hour": 3600
}

time_label = st.selectbox("Transaction Time", list(time_options.keys()))
time = time_options[time_label]

transaction_type = st.selectbox(
    "Transaction Type",
    ["Online", "POS", "ATM"]
)

location_risk = st.selectbox(
    "Location Risk",
    ["Low", "Medium", "High"]
)

device_type = st.selectbox(
    "Device Used",
    ["Mobile", "Desktop", "Tablet"]
)

if st.button("Check Fraud Risk"):

    try:

        # Create base feature vector (31 features)
        features = [0]*31

        # Time
        features[0] = time

        # Amount scaling (to avoid false anomalies)
        features[-1] = amount / 1000

        # Simulated normal behaviour patterns
        features[1] = np.random.normal(0,0.1)
        features[2] = np.random.normal(0,0.1)
        features[3] = np.random.normal(0,0.1)

        if location_risk == "High":
            features[4] = -1.5
        elif location_risk == "Medium":
            features[4] = -0.5
        else:
            features[4] = 0.2

        if transaction_type == "Online":
            features[5] = -0.8
        else:
            features[5] = 0.2

        # ML prediction
        result, risk_score = predict(features)

        st.subheader("Fraud Risk Score")

        st.progress(risk_score/100)

        st.metric("Risk Score", f"{risk_score:.2f}%")

        # Fraud threshold
        if risk_score >= 70:
            st.error("⚠ FRAUD DETECTED")
        else:
            st.success("✅ Normal Transaction")

        # Chart visualization
        st.subheader("Transaction Feature Pattern")

        fig, ax = plt.subplots()

        ax.plot(features, marker="o")

        ax.set_xlabel("Feature Index")
        ax.set_ylabel("Value")

        st.pyplot(fig)

    except Exception as e:
        st.warning(e)


# ------------------------------------------------
# OPTION 2 : COPY-PASTE VECTOR (Developers)
# ------------------------------------------------

st.header("Advanced Mode (Paste Feature Vector)")

vector_input = st.text_area(
    "Paste 31 comma-separated values",
    "3600,0.1,0.05,0.02,0.01,0.03,0.04,0.02,0.01,0.03,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.01,120"
)

if st.button("Check Pasted Transaction"):

    try:

        features = [float(x) for x in vector_input.split(",")]

        result, risk_score = predict(features)

        st.subheader("Fraud Risk Score")

        st.progress(risk_score/100)

        st.metric("Risk Score", f"{risk_score:.2f}%")

        if risk_score >= 70:
            st.error("⚠ FRAUD DETECTED")
        else:
            st.success("✅ Normal Transaction")

    except Exception as e:
        st.warning(e)


# ------------------------------------------------
# OPTION 3 : MANUAL FEATURE ENTRY (Testing)
# ------------------------------------------------

st.header("Manual Feature Input (Testing)")

manual_features = []

for i in range(31):

    val = st.number_input(f"Feature {i+1}", value=0.0, key=i)

    manual_features.append(val)

if st.button("Check Manual Transaction"):

    try:

        result, risk_score = predict(manual_features)

        st.subheader("Fraud Risk Score")

        st.progress(risk_score/100)

        st.metric("Risk Score", f"{risk_score:.2f}%")

        if risk_score >= 70:
            st.error("⚠ FRAUD DETECTED")
        else:
            st.success("✅ Normal Transaction")

    except Exception as e:
        st.warning(e)