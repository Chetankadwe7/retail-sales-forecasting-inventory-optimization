from src.data_loader import generate_data
from src.preprocessing import clean_data
from src.features import create_features
from src.model import train_model
from src.inventory import calculate_inventory

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data
df = generate_data()

# -------------------------------
# Sales Trend Graph (ADD THIS)
# -------------------------------
daily_sales = df.groupby("date")["qty_sold"].sum()

plt.figure()
plt.plot(daily_sales)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Quantity Sold")
plt.show()

# Step 2: Clean
df = clean_data(df)

# Step 3: Features
df = create_features(df)

# Step 4: Model
model, pred, y = train_model(df)

# Step 5: Inventory
SS, ROP = calculate_inventory(pred, y)

print("Safety Stock:", round(SS, 2))
print("Reorder Point:", round(ROP, 2))

# Save outputs
forecast_df = pd.DataFrame({
    "Actual": y.values,
    "Predicted": pred
})
forecast_df.to_csv("outputs/forecast.csv", index=False)

inventory_df = pd.DataFrame({
    "Safety Stock": [SS],
    "Reorder Point": [ROP]
})
inventory_df.to_csv("outputs/inventory.csv", index=False)

print("Outputs saved ✅")

# -------------------------------
# Prediction Graph
# -------------------------------
plt.figure()
plt.plot(y.values, label="Actual")
plt.plot(pred, label="Predicted")
plt.legend()
plt.title("Actual vs Predicted")
plt.show()