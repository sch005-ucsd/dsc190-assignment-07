import pandas as pd
from dateutil import parser as dateparser
import os

VALID_TYPES = {"click", "view", "scroll", "login", "purchase"}

df = pd.read_csv("data/raw/events.csv")

# Drop rows with any missing fields
df = df.dropna()
df = df[df["user_id"].astype(str).str.strip() != ""]
df = df[df["timestamp"].astype(str).str.strip() != ""]
df = df[df["event_type"].astype(str).str.strip() != ""]
df = df[df["duration_seconds"].astype(str).str.strip() != ""]

# Convert duration_seconds to numeric, drop non-numeric
df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df.dropna(subset=["duration_seconds"])

# Drop invalid event_type (case-sensitive exact match)
df = df[df["event_type"].isin(VALID_TYPES)]

# Drop non-positive duration_seconds
df = df[df["duration_seconds"] > 0]

# Convert to int
df["duration_seconds"] = df["duration_seconds"].astype(int)

# Normalize timestamp to ISO 8601 YYYY-MM-DDTHH:MM:SS
def normalize_ts(ts):
    return dateparser.parse(str(ts)).strftime("%Y-%m-%dT%H:%M:%S")

df["timestamp"] = df["timestamp"].apply(normalize_ts)

os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/events.csv", index=False)
print(f"Clean: {len(df)} rows written")
