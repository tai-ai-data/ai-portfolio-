from cleaning import clean_data
from feature_engineering import apply_feature_engineering
from modeling import train_model

def run_pipeline(df, target_column):
    """
    Full ML pipeline: cleaning → feature engineering → modeling.
    """
    # 1. Clean data
    df = clean_data(df)

    # 2. Feature engineering
    df = apply_feature_engineering(df)

    # 3. Split features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # 4. Train model
    model, accuracy = train_model(X, y)

    return model, accuracy
