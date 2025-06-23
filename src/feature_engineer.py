import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates additional features required for CLV prediction.

    Parameters:
        df (pd.DataFrame): Cleaned input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with additional engineered features.
    """

    # --- RFM Features ---
    df['Recency'] = df['DaysSinceLastPurchase']
    df['Frequency'] = df['TotalPurchases']
    df['Monetary'] = df['TotalRevenue']

    # --- Tenure (days since signup) ---
    today = pd.Timestamp.today()
    df['TenureDays'] = (today - df['SignupDate']).dt.days

    # --- Behavior Ratios ---
    df['ClicksPerVisit'] = df.apply(
        lambda row: row['EmailClicks'] / row['WebsiteVisits'] if row['WebsiteVisits'] > 0 else 0,
        axis=1
    )

    df['RevenuePerVisit'] = df.apply(
        lambda row: row['TotalRevenue'] / row['WebsiteVisits'] if row['WebsiteVisits'] > 0 else 0,
        axis=1
    )

    # --- Categorical Encoding (if needed later) ---
    df['Gender'] = df['Gender'].map({'F': 0, 'M': 1})
    df['CountryEncoded'] = df['Country'].astype('category').cat.codes

    # Optional: drop raw text features if encoding is used
    # df = df.drop(columns=['Country', 'Gender'])

    return df

# Example usage
if __name__ == "__main__":
    from data_cleaner import clean_data

    # Load and clean sample data
    df_cleaned = clean_data("data/sample_data.csv")
    df_features = create_features(df_cleaned)
    print(df_features.head())
