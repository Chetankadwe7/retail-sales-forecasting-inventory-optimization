import pandas as pd

def create_features(df):
    df = df.sort_values("date")

    df["lag_1"] = df["qty_sold"].shift(1)
    df["lag_7"] = df["qty_sold"].shift(7)

    df["rolling_mean_7"] = df["qty_sold"].shift(1).rolling(7).mean()
    df["rolling_std_7"] = df["qty_sold"].shift(1).rolling(7).std()

    df["day_of_week"] = pd.to_datetime(df["date"]).dt.dayofweek
    df["month"] = pd.to_datetime(df["date"]).dt.month

    return df.dropna()