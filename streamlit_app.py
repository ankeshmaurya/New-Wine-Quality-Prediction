
import streamlit as st
import joblib
import json
import pandas as pd

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="centered"
)

st.title("🍷 Wine Quality Prediction App")
st.write(
    "Enter the physicochemical properties of the wine "
    "to predict its quality."
)

# --------------------------------------------------
# Load model and schema
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("wine_model.pkl")


@st.cache_data
def load_schema():
    with open("wine_schema.json", "r") as f:
        return json.load(f)


model = load_model()
schema = load_schema()

# --------------------------------------------------
# Sidebar inputs
# --------------------------------------------------

st.sidebar.header("🍷 Wine Features")

features = {}

for feature in schema["features"]:

    low, high = schema["feature_ranges"][feature]

    features[feature] = st.sidebar.slider(
        feature,
        min_value=float(low),
        max_value=float(high),
        value=float((low + high) / 2)
    )

# --------------------------------------------------
# Create input DataFrame
# --------------------------------------------------

df = pd.DataFrame([features])

# Ensure exact feature order
df = df[schema["features"]]

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Quality", type="primary"):

    try:

        # Prediction
        pred = model.predict(df)[0]

        # Probability
        proba = model.predict_proba(df)[0]

        # --------------------------------------------------
        # Quality category
        # --------------------------------------------------

        if pred <= 4:
            quality_label = "Bad ❌"

        elif pred <= 6:
            quality_label = "Good ✅"

        else:
            quality_label = "Best 🏆"

        # --------------------------------------------------
        # Display prediction
        # --------------------------------------------------

        st.success(
            f"Predicted Quality: **{pred}** → {quality_label}"
        )

        # --------------------------------------------------
        # Probability
        # --------------------------------------------------

        st.subheader("Prediction Probability")

        probability_df = pd.DataFrame(
            {
                "Quality": [str(c) for c in model.classes_],
                "Probability": proba
            }
        )

        probability_df = probability_df.set_index("Quality")

        st.bar_chart(probability_df)

        # --------------------------------------------------
        # Show input
        # --------------------------------------------------

        with st.expander("View Input Values"):

            st.dataframe(
                df,
                use_container_width=True
            )

    except Exception as e:

        st.error(
            "Prediction failed. Please check the deployed "
            "Python/scikit-learn environment."
        )

        st.exception(e)

