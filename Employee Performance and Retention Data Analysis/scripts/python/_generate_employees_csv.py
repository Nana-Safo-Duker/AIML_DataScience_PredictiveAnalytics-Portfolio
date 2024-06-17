"""Generate synthetic employees.csv for educational pipeline demos."""
import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rng = np.random.default_rng(42)

n = 1000
first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
    "Timothy", "Deborah", "Ronald", "Stephanie", "Edward", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Angela", "Eric", "Shirley", "Jonathan", "Anna", "Stephen", "Brenda",
]
teams = [
    "Marketing", "Client Services", "Product", "Legal", "Engineering", "Finance",
    "Human Resources", "Sales", "Business Development", "Distribution",
]
genders = ["Male", "Female"]

start_base = datetime(1995, 1, 1)
start_end = datetime(2023, 12, 31)
span_days = (start_end - start_base).days

rows = []
for _ in range(n):
    gender = rng.choice(genders)
    senior = rng.choice(["true", "false"], p=[0.22, 0.78])
    team = rng.choice(teams)
    start = start_base + timedelta(days=int(rng.integers(0, span_days + 1)))
    hour = int(rng.integers(0, 24))
    minute = int(rng.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]))
    login_dt = datetime(2000, 1, 1, hour, minute)
    base_salary = 45000 + int(rng.normal(35000, 18000))
    if senior == "true":
        base_salary += int(rng.integers(15000, 45000))
    team_bump = {
        "Engineering": 12000, "Legal": 10000, "Finance": 8000, "Product": 7000,
        "Sales": 5000, "Business Development": 6000, "Marketing": 3000,
        "Client Services": 2000, "Human Resources": 1000, "Distribution": 0,
    }[team]
    salary = max(32000, base_salary + team_bump + int(rng.integers(-5000, 8000)))
    bonus = float(np.clip(rng.normal(10.5 if senior == "true" else 8.0, 3.5), 0.5, 25.0))
    rows.append({
        "First Name": rng.choice(first_names),
        "Gender": gender,
        "Senior Management": senior,
        "Team": team,
        "Start Date": start.strftime("%m/%d/%Y"),
        "Last Login Time": login_dt.strftime("%I:%M %p").lstrip("0"),
        "Salary": salary,
        "Bonus %": round(bonus, 3),
    })

df = pd.DataFrame(rows)

# Inject missing values to exercise cleaning
miss_idx = rng.choice(n, size=45, replace=False)
df.loc[miss_idx[:12], "First Name"] = np.nan
df.loc[miss_idx[12:27], "Gender"] = np.nan
df.loc[miss_idx[27:35], "Senior Management"] = np.nan
df.loc[miss_idx[35:42], "Team"] = np.nan
df.loc[miss_idx[42:45], "Salary"] = np.nan
bonus_miss = rng.choice(n, size=20, replace=False)
df.loc[bonus_miss, "Bonus %"] = np.nan

out_path = os.path.join(project_root, "data", "raw", "employees.csv")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
df.to_csv(out_path, index=False)
print(f"Wrote {out_path} shape={df.shape}")
print(df.isnull().sum())
