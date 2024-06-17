# Data Directory

This directory contains the fraud detection dataset.

## Files

- `fraud_data.csv` — Compact **synthetic educational sample** (IEEE-CIS–style columns) so EDA and ML scripts can run without the original full dataset.

## Note on provenance

The original `fraud_data.csv` was **not committed** to this repository (size/license). The included file is randomly generated with a fixed RNG seed: imbalanced `isFraud`, `TransactionAmt`, `TransactionDT`, card/address fields, `C1–C5`, `D1–D5`, `V1–V20`, and categoricals (`ProductCD`, `DeviceType`, `M1–M3`, etc.). It is for educational demos only—not real transactions.

## Target Variable

- `isFraud` — Binary target (0 = legitimate, 1 = fraudulent)

## Features (sample schema)

- Transaction: `TransactionAmt`, `TransactionDT`, `ProductCD`
- Card / address: `card1`–`card5`, `card4`, `addr1`, `addr2`, `dist1`, `dist2`
- Counts / deltas / engineered: `C1`–`C5`, `D1`–`D5`, `V1`–`V20`
- Match / device: `M1`–`M3`, `DeviceType`

## Data Usage

Use for educational and research practice only. Do not treat rows as real financial activity.
