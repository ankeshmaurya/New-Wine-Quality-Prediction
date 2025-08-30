import streamlit as st
import joblib, json
import pandas as pd

st.set_page_config(page_title="Wine Quality Prediction", page_icon="🍷", layout="centered")

st.title("🍷 Wine Quality Prediction App")

# Load model and schema
model = joblib.load("wine_model.pkl")
schema = json.load(open("wine_schema.json"))

# Sidebar input
st.sidebar.header("Input Features")
features = {}
for f in schema["features"]:
    low, high = schema["feature_ranges"][f]
    features[f] = st.sidebar.slider(f, float(low), float(high), float((low+high)/2))

df = pd.DataFrame([features])

# Prediction
if st.button("Predict Quality"):
    proba = model.predict_proba(df)[0]
    pred = model.predict(df)[0]

    # Categorize wine quality
    if pred <= 4:
        quality_label = "Bad ❌"
    elif 5 <= pred <= 6:
        quality_label = "Good ✅"
    else:  # 7 and above
        quality_label = "Best 🏆"

    st.success(f"Predicted Quality: {pred} → {quality_label}")
    st.bar_chart({str(c): p for c, p in zip(model.classes_, proba)})
