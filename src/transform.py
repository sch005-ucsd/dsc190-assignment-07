import pandas as pd

df = pd.read_csv("data/clean/events.csv")

df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

df.to_csv("data/transformed/events.csv", index=False)
print(f"Transform: {len(df)} rows written")
