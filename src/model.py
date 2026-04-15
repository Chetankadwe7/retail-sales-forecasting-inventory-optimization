from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(df):

    features = [
        "lag_1", "lag_7",
        "rolling_mean_7", "rolling_std_7",
        "day_of_week", "month"
    ]

    X = df[features]
    y = df["qty_sold"]

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X, y)

    pred = model.predict(X)

    joblib.dump(model, "models/rf_model.pkl")

    return model, pred, y