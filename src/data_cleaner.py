import pandas as pd
from datetime import datetime

def clean_data(filepath: str) -> pd.DataFrame:
    """
    Cleans and preprocesses raw customer data for CLV modeling.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame ready for feature engineering.
    """
    # Load dataset
    df = pd.read_csv(filepath)

    # Convert date columns to datetime
    df['SignupDate'] = pd.to_datetime(df['SignupDate'], errors='coerce')
    df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'], errors='coerce')

    # Fill missing values (if any)
    df['EmailClicks'] = df['EmailClicks'].fillna(0)
    df['WebsiteVisits'] = df['WebsiteVisits'].fillna(0)
    df['TotalPurchases'] = df['TotalPurchases'].fillna(0)
    df['TotalRevenue'] = df['TotalRevenue'].fillna(0)

    # Drop rows with critical missing values
    df.dropna(subset=['CustomerID', 'SignupDate', 'LastPurchaseDate'], inplace=True)

    # Recalculate AvgOrderValue if missing or incorrect
    df['AvgOrderValue'] = df.apply(
        lambda row: row['TotalRevenue'] / row['TotalPurchases'] if row['TotalPurchases'] > 0 else 0,
        axis=1
    )

    # Ensure proper types
    df['CustomerID'] = df['CustomerID'].astype(str)
    df['Gender'] = df['Gender'].astype('category')
    df['Country'] = df['Country'].astype('category')

    # Calculate DaysSinceLastPurchase from today
    today = pd.to_datetime(datetime.today().date())
    df['DaysSinceLastPurchase'] = (today - df['LastPurchaseDate']).dt.days

    return df

# Sample usage (during testing)
if __name__ == "__main__":
    cleaned_df = clean_data("data/sample_data.csv")
    print(cleaned_df.head())
