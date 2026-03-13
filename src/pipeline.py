import os
import joblib
import numpy as np

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load models
iso = joblib.load(os.path.join(MODEL_DIR, "iso_model.pkl"))
svm = joblib.load(os.path.join(MODEL_DIR, "svm_model.pkl"))
db = joblib.load(os.path.join(MODEL_DIR, "db_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))


def pipeline(data):

    if len(data) != 31:
        raise ValueError(f"Expected 31 features but got {len(data)}")

    data = np.array(data).reshape(1, -1)

    data_scaled = scaler.transform(data)

    iso_pred = iso.predict(data_scaled)
    svm_pred = svm.predict(data_scaled)
    db_pred = db.fit_predict(data_scaled)

    iso_pred = 1 if iso_pred[0] == -1 else 0
    svm_pred = 1 if svm_pred[0] == -1 else 0
    db_pred = 1 if db_pred[0] == -1 else 0

    votes = iso_pred + svm_pred + db_pred

    risk_score = (votes / 3) * 100

    if risk_score >= 60:
        return "fraud", risk_score
    else:
        return "normal", risk_score

