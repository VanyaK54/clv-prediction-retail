import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

from data_cleaner import clean_data
from feature_engineer import create_features

def train_model(input_path="data/sample_data.csv", model_path="models/clv_model.pkl"):
    """
    Trains a Random Forest regression model to predict Customer Lifetime Value (CLV).

    Parameters:
        input_path (str): Path to cleaned data.
        model_path (str): Path to save the trained model.
    """

    # Load and process data
    df = clean_data(input_path)
    df = create_features(df)

    # Target variable (Monetary = proxy for CLV)
    y = df['Monetary']

    # Feature selection
    feature_cols = [
        'Recency', 'Frequency', 'TenureDays',
        'ClicksPerVisit', 'RevenuePerVisit',
        'Gender', 'CountryEncoded'
    ]
    X = df[feature_cols]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    print(f"Model trained ✅\nRMSE: {rmse:.2f}, R²: {r2:.2f}")

    # Save model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
