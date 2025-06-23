import pandas as pd
import joblib
from data_cleaner import clean_data
from feature_engineer import create_features

def predict_clv(new_data_path="data/sample_data.csv", model_path="models/clv_model.pkl"):
    """
    Predicts CLV for new customer data using a pre-trained model.

    Parameters:
        new_data_path (str): Path to the new customer data CSV.
        model_path (str): Path to the trained model file.
    """

    # Load and prepare new data
    df_new = clean_data(new_data_path)
    df_new = create_features(df_new)

    # Features used for prediction (same as training)
    feature_cols = [
        'Recency', 'Frequency', 'TenureDays',
        'ClicksPerVisit', 'RevenuePerVisit',
        'Gender', 'CountryEncoded'
    ]

    X_new = df_new[feature_cols]

    # Load trained model
    model = joblib.load(model_path)

    # Predict
    predictions = model.predict(X_new)

    # Append predictions to dataframe
    df_new['Predicted_CLV'] = predictions

    return df_new[['CustomerID', 'Predicted_CLV'] + feature_cols]

# Sample usage
if __name__ == "__main__":
    results = predict_clv()
    print("CLV Predictions:\n", results.head())
