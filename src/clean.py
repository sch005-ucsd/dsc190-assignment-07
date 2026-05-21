import pandas as pd
from dateutil import parser as dateparser

VALID_TYPES = {"click", "view", "purchase"}

df = pd.read_csv("data/raw/events.csv")

# Drop rows with any missing fields
df = df.dropna()

# Drop invalid event_type
df = df[df["event_type"].isin(VALID_TYPES)]

# Drop non-positive duration_seconds
df = df[df["duration_seconds"] > 0]

# Normalize timestamp to ISO 8601 YYYY-MM-DDTHH:MM:SS
def normalize_ts(ts):
    return dateparser.parse(str(ts)).strftime("%Y-%m-%dT%H:%M:%S")

df["timestamp"] = df["timestamp"].apply(normalize_ts)

df.to_csv("data/clean/events.csv", index=False)
print(f"Clean: {len(df)} rows written")
