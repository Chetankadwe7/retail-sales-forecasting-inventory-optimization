import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=200)

    data = []

    for store in range(1, 4):
        for item in range(101, 106):
            base_demand = np.random.randint(15, 30)

            for date in dates:
                demand = base_demand + np.random.randint(-5, 10)

                on_promo = np.random.choice([0, 1], p=[0.8, 0.2])
                if on_promo:
                    demand += np.random.randint(5, 15)

                demand = max(0, demand)
                price = np.random.randint(50, 200)

                data.append([date, store, item, demand, price, on_promo])

    df = pd.DataFrame(data, columns=[
        "date", "store_id", "item_id", "qty_sold", "price", "on_promo"
    ])

    df.to_csv("data/retail_data.csv", index=False)

    return df