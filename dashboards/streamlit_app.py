import streamlit as st
import pandas as pd
import joblib

from src.data_cleaner import clean_data
from src.feature_engineer import create_features

st.title("🛍️ Customer Lifetime Value (CLV) Predictor")

uploaded_file = st.file_uploader("Upload Customer CSV File", type=["csv"])

if uploaded_file:
    df_input = pd.read_csv(uploaded_file)
    df_clean = clean_data(uploaded_file)
    df_feat = create_features(df_clean)

    model = joblib.load("models/clv_model.pkl")

    feature_cols = [
        'Recency', 'Frequency', 'TenureDays',
        'ClicksPerVisit', 'RevenuePerVisit',
        'Gender', 'CountryEncoded'
    ]
    df_feat['Predicted_CLV'] = model.predict(df_feat[feature_cols])

    st.subheader("📈 Predicted CLV Results")
    st.dataframe(df_feat[['CustomerID', 'Predicted_CLV'] + feature_cols])

    st.download_button(
        "📥 Download Predictions as CSV",
        df_feat.to_csv(index=False),
        file_name="predicted_clv.csv",
        mime="text/csv"
    )
