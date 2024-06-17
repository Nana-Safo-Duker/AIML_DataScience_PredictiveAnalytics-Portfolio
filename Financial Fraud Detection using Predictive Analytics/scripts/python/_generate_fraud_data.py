"""Generate compact synthetic IEEE-CIS-style fraud_data.csv for educational demos."""
from pathlib import Path

import numpy as np
import pandas as pd

project_root = Path(__file__).resolve().parent.parent.parent
rng = np.random.default_rng(42)

n = 8000
fraud_rate = 0.02
n_fraud = int(n * fraud_rate)
is_fraud = np.zeros(n, dtype=int)
is_fraud[:n_fraud] = 1
rng.shuffle(is_fraud)

product_cds = ["W", "C", "R", "H", "S"]
device_types = ["desktop", "mobile"]
m_vals = ["T", "F"]
card4_vals = ["visa", "mastercard", "discover", "american express"]

# Base features with mild fraud signal
transaction_amt = rng.lognormal(mean=3.8, sigma=0.9, size=n)
transaction_amt = np.clip(transaction_amt, 1.0, 5000.0)
# Fraud tends slightly higher / more variable amounts
transaction_amt = np.where(
    is_fraud == 1,
    transaction_amt * rng.uniform(1.1, 2.8, size=n),
    transaction_amt,
)

transaction_dt = rng.integers(86400, 86400 * 180, size=n)
card1 = rng.integers(1000, 18000, size=n)
card2 = rng.choice(np.arange(100.0, 600.0, 1.0), size=n)
card3 = rng.choice([150.0, 185.0], size=n, p=[0.85, 0.15])
card5 = rng.choice([100.0, 102.0, 117.0, 138.0, 142.0, 150.0, 162.0, 166.0, 224.0, 226.0], size=n)
addr1 = rng.choice(np.arange(100.0, 500.0, 1.0), size=n)
addr2 = rng.choice([87.0, 60.0, 96.0], size=n, p=[0.9, 0.05, 0.05])
dist1 = rng.exponential(scale=80, size=n)
dist2 = rng.exponential(scale=120, size=n)

data = {
    "isFraud": is_fraud,
    "TransactionAmt": np.round(transaction_amt, 3),
    "TransactionDT": transaction_dt,
    "ProductCD": rng.choice(product_cds, size=n, p=[0.55, 0.15, 0.12, 0.1, 0.08]),
    "card1": card1,
    "card2": card2,
    "card3": card3,
    "card4": rng.choice(card4_vals, size=n, p=[0.55, 0.32, 0.08, 0.05]),
    "card5": card5,
    "addr1": addr1,
    "addr2": addr2,
    "dist1": dist1,
    "dist2": dist2,
    "DeviceType": rng.choice(device_types, size=n, p=[0.65, 0.35]),
}

for i in range(1, 4):
    data[f"M{i}"] = rng.choice(m_vals, size=n)

for i in range(1, 6):
    # C features: counts; fraud slightly elevated
    base = rng.poisson(lam=2.5 + i * 0.3, size=n).astype(float)
    data[f"C{i}"] = np.where(is_fraud == 1, base + rng.poisson(2, size=n), base)

for i in range(1, 6):
    # D features: days deltas with missingness
    vals = rng.exponential(scale=30 + i * 5, size=n)
    data[f"D{i}"] = vals

for i in range(1, 21):
    # V features: anonymous engineered numerics
    mu = 0.5 if is_fraud.mean() else 0.0
    vals = rng.normal(loc=0.0, scale=1.0 + i * 0.02, size=n)
    vals = np.where(is_fraud == 1, vals + rng.normal(0.6, 0.4, size=n), vals)
    data[f"V{i}"] = vals

df = pd.DataFrame(data)

# Inject missing values (common in IEEE-CIS style)
for col, rate in [
    ("card2", 0.08), ("card3", 0.05), ("card5", 0.06), ("addr1", 0.12),
    ("addr2", 0.15), ("dist1", 0.35), ("dist2", 0.55), ("D1", 0.1),
    ("D2", 0.25), ("D3", 0.3), ("D4", 0.28), ("D5", 0.32),
    ("M1", 0.2), ("M2", 0.22), ("M3", 0.25), ("DeviceType", 0.05),
]:
    mask = rng.random(n) < rate
    df.loc[mask, col] = np.nan

# A few V features with missingness
for i in [3, 7, 12, 18]:
    mask = rng.random(n) < 0.15
    df.loc[mask, f"V{i}"] = np.nan

# Slight ProductCD fraud association
fraud_idx = df.index[df["isFraud"] == 1]
df.loc[fraud_idx, "ProductCD"] = rng.choice(
    product_cds, size=len(fraud_idx), p=[0.25, 0.35, 0.2, 0.12, 0.08]
)

out_path = project_root / "data" / "fraud_data.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False)
print(f"Wrote {out_path} shape={df.shape}")
print(f"Fraud rate: {df['isFraud'].mean():.4f}")
print(f"Columns ({len(df.columns)}): {list(df.columns)}")
print(f"Missing total: {df.isnull().sum().sum()}")
