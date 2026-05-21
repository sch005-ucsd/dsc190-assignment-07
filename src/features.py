import pandas as pd
import os

df = pd.read_csv("data/transformed/events.csv")

df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

os.makedirs("data/features", exist_ok=True)
df.to_csv("data/features/events.csv", index=False)
print(f"Features: {len(df)} rows written")
