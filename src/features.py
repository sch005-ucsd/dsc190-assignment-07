import pandas as pd

df = pd.read_csv("data/transformed/events.csv")

df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

df.to_csv("data/features/events.csv", index=False)
print(f"Features: {len(df)} rows written")
