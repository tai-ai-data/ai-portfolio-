import pandas as pd

def apply_feature_engineering(df):
    """
    Apply all feature engineering steps.
    """
    # Example placeholder — we will upgrade this later
    df["TotalChargesPerMonth"] = df["TotalCharges"] / (df["tenure"] + 1)
    return df
