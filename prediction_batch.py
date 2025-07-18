import io
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import csv
import shap
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from custom_components import pre_preprocessing, normalize_ordinal_columns
from io import BytesIO
from sklearn.pipeline import Pipeline

# === Utils ===
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Predictions')
    output.seek(0)
    return output

# === Load model and pipeline ===
def load_pipeline():
    try:
        with open("pipelines.pkl", "rb") as f:
            saved = pickle.load(f)
            model = saved["model"]
            preprocessing = saved["preprocessing"]
            pipeline = Pipeline([
                ("preprocessing", preprocessing),
                ("model", model)
            ])
            st.session_state["pipeline"] = pipeline
            st.session_state["feature_names"] = preprocessing[:-1].get_feature_names_out()
            return pipeline
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None

# === App Main ===
def app():
    tab1, tab2 = st.tabs(["📁 Prediction", "📈 Results"])

    pipeline = st.session_state.get("pipeline") or load_pipeline()
    if pipeline is None:
        return

    with tab1:
        required_cols = [
            "type_heater", "basements", "topography", "homestead_exemption",
            "geographic_ward", "garage_type", "parcel_shape", "view_type",
            "interior_condition", "exterior_condition", "zoning", "off_street_open",
            "year_built", "number_of_bathrooms", "number_of_bedrooms", "total_livable_area",
            "number_of_rooms", "number_stories", "total_area", "frontage", "depth", "fireplaces"
        ]
        st.markdown(f"Upload an Excel or CSV file with property data to predict house values. **Required columns**: `{', '.join(required_cols)}`.")

        uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
                st.subheader("📄 Uploaded Data Preview")
                st.dataframe(df.head())

                missing = [col for col in required_cols if col not in df.columns]
                if missing:
                    st.error(f"⚠️ Missing required columns: {missing}")
                    return

                if st.button("🔮 Predict All"):
                    transformed = pipeline.named_steps["preprocessing"].transform(df)
                    preds = pipeline.named_steps["model"].predict(transformed)
                    df["predicted_value"] = preds
                    st.session_state["prediction_df"] = df

                    st.subheader("🎯 Prediction Results")
                    st.dataframe(df[required_cols + ["predicted_value"]])

                    st.download_button(
                        label="📥 Download Results",
                        data=to_excel(df),
                        file_name="house_price_predictions.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            except Exception as e:
                st.error(f"❌ Failed to process file: {e}")

    with tab2:
        st.write("Under Development")

