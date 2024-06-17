"""
Comprehensive Exploratory Data Analysis (EDA) for Iris Dataset
Author: Data Science Project
Date: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load data
data_path = Path(__file__).parent.parent.parent / 'data' / 'Iris.csv'
df = pd.read_csv(data_path)

print("=" * 80)
print("EXPLORATORY DATA ANALYSIS - IRIS DATASET")
print("=" * 80)

# 1. Dataset Overview
print("\n1. DATASET OVERVIEW")
print("-" * 80)
print(f"Dataset shape: {df.shape}")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"\nColumn names: {list(df.columns)}")
print(f"\nData types:\n{df.dtypes}")

# 2. First and Last Few Rows
print("\n2. FIRST FEW ROWS")
print("-" * 80)
print(df.head(10))
print("\nLAST FEW ROWS")
print("-" * 80)
print(df.tail(10))

# 3. Basic Statistics
print("\n3. DESCRIPTIVE STATISTICS")
print("-" * 80)
print(df.describe())

# 4. Missing Values
print("\n4. MISSING VALUES")
print("-" * 80)
missing = df.isnull().sum()
print(missing)
print(f"\nTotal missing values: {missing.sum()}")

# 5. Data Types Information
print("\n5. DATA TYPES INFORMATION")
print("-" * 80)
print(df.info())

# 6. Target Variable Distribution
print("\n6. TARGET VARIABLE DISTRIBUTION")
print("-" * 80)
print(df['variety'].value_counts())
print(f"\nProportions:\n{df['variety'].value_counts(normalize=True)}")

# 7. Visualizations
print("\n7. GENERATING VISUALIZATIONS...")
print("-" * 80)

# Create results directory
results_dir = Path(__file__).parent.parent.parent / 'results'
results_dir.mkdir(exist_ok=True)
figures_dir = results_dir / 'figures'
figures_dir.mkdir(exist_ok=True)

# 7.1 Pair Plot
print("Creating pair plot...")
sns.pairplot(df, hue='variety', diag_kind='hist')
plt.suptitle('Pair Plot of Iris Dataset', y=1.02, fontsize=16)
plt.savefig(figures_dir / 'pairplot.png', dpi=300, bbox_inches='tight')
plt.close()

# 7.2 Distribution of each feature by species
print("Creating distribution plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
features = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']

for idx, feature in enumerate(features):
    ax = axes[idx // 2, idx % 2]
    for variety in df['variety'].unique():
        data = df[df['variety'] == variety][feature]
        ax.hist(data, alpha=0.6, label=variety, bins=20)
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of {feature}')
    ax.legend()

plt.tight_layout()
plt.savefig(figures_dir / 'feature_distributions.png', dpi=300, bbox_inches='tight')
plt.close()

# 7.3 Box plots
print("Creating box plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
for idx, feature in enumerate(features):
    ax = axes[idx // 2, idx % 2]
    sns.boxplot(x='variety', y=feature, data=df, ax=ax)
    ax.set_title(f'Box Plot of {feature} by Variety')
    ax.set_xlabel('Variety')
    ax.set_ylabel(feature)

plt.tight_layout()
plt.savefig(figures_dir / 'boxplots.png', dpi=300, bbox_inches='tight')
plt.close()

# 7.4 Correlation Heatmap
print("Creating correlation heatmap...")
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix of Iris Dataset Features')
plt.tight_layout()
plt.savefig(figures_dir / 'correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 7.5 Violin plots
print("Creating violin plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
for idx, feature in enumerate(features):
    ax = axes[idx // 2, idx % 2]
    sns.violinplot(x='variety', y=feature, data=df, ax=ax)
    ax.set_title(f'Violin Plot of {feature} by Variety')
    ax.set_xlabel('Variety')
    ax.set_ylabel(feature)

plt.tight_layout()
plt.savefig(figures_dir / 'violin_plots.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. Outlier Detection
print("\n8. OUTLIER DETECTION (IQR Method)")
print("-" * 80)
for feature in features:
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    print(f"\n{feature}:")
    print(f"  Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"  Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
    print(f"  Number of outliers: {len(outliers)}")

# 9. Summary Statistics by Variety
print("\n9. SUMMARY STATISTICS BY VARIETY")
print("-" * 80)
for variety in df['variety'].unique():
    print(f"\n{variety}:")
    print(df[df['variety'] == variety][features].describe())

print("\n" + "=" * 80)
print("EDA COMPLETE! Visualizations saved to results/figures/ directory")
print("=" * 80)





