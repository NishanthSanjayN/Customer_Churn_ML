import streamlit as st
import pandas as pd
import pickle

# ================================
# LOAD MODEL & COLUMNS
# ================================
model = pickle.load(open("churn_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction App")
st.write("Fill customer details below:")

# ================================
# USER INPUTS (FULL FEATURES)
# ================================
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
phone = st.selectbox("Phone Service", ["Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check",
     "Bank transfer (automatic)", "Credit card (automatic)"]
)

# ================================
# CREATE INPUT DATAFRAME
# ================================
input_dict = {
    "tenure": tenure,
    "MonthlyCharges": monthly,
    "TotalCharges": total,
    "SeniorCitizen": senior,
    "gender": gender,
    "Partner": partner,
    "Dependents": dependents,
    "PhoneService": phone,
    "InternetService": internet,
    "Contract": contract,
    "PaymentMethod": payment
}

input_df = pd.DataFrame([input_dict])

# ================================
# ENCODING + ALIGNMENT
# ================================
input_df = pd.get_dummies(input_df)
input_df = input_df.reindex(columns=columns, fill_value=0)

# ================================
# PREDICTION
# ================================
if st.button("Predict Churn"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Result:")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn ({probability:.2f})")
    else:
        st.success(f"✅ Low Risk ({probability:.2f})")

    # Progress bar for probability
    st.progress(int(probability * 100))

# ================================
# BULK CSV PREDICTION
# ================================
st.subheader("📂 Bulk Prediction")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    data = pd.get_dummies(data)
    data = data.reindex(columns=columns, fill_value=0)

    preds = model.predict(data)
    data["Churn Prediction"] = preds

    st.write(data.head())

    st.download_button(
        "Download Results",
        data.to_csv(index=False),
        "predictions.csv"
    )