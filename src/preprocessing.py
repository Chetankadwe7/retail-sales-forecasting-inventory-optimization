def clean_data(df):
    df = df.dropna()
    df = df[df["qty_sold"] >= 0]
    return df