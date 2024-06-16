"""
Univariate Analysis for Iris Dataset
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load data
data_path = Path(__file__).parent.parent.parent / 'data' / 'Iris.csv'
df = pd.read_csv(data_path)
features = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']

print("=" * 80)
print("UNIVARIATE ANALYSIS - IRIS DATASET")
print("=" * 80)

# Create results directory
results_dir = Path(__file__).parent.parent.parent / 'results'
results_dir.mkdir(exist_ok=True)
figures_dir = results_dir / 'figures'
figures_dir.mkdir(exist_ok=True)

# 1. Descriptive Statistics
print("\n1. DESCRIPTIVE STATISTICS")
print("-" * 80)
for feature in features:
    print(f"\n{feature}:")
    print(f"  Mean: {df[feature].mean():.3f}")
    print(f"  Median: {df[feature].median():.3f}")
    print(f"  Std Dev: {df[feature].std():.3f}")
    print(f"  Variance: {df[feature].var():.3f}")
    print(f"  Min: {df[feature].min():.3f}")
    print(f"  Max: {df[feature].max():.3f}")
    print(f"  Range: {df[feature].max() - df[feature].min():.3f}")
    print(f"  IQR: {df[feature].quantile(0.75) - df[feature].quantile(0.25):.3f}")
    print(f"  Skewness: {df[feature].skew():.3f}")
    print(f"  Kurtosis: {df[feature].kurtosis():.3f}")

# 2. Distribution Plots
print("\n2. GENERATING DISTRIBUTION PLOTS...")
print("-" * 80)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
for idx, feature in enumerate(features):
    ax = axes[idx // 2, idx % 2]
    ax.hist(df[feature], bins=30, edgecolor='black', alpha=0.7)
    ax.axvline(df[feature].mean(), color='r', linestyle='--', label='Mean')
    ax.axvline(df[feature].median(), color='g', linestyle='--', label='Median')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of {feature}')
    ax.legend()
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(figures_dir / 'univariate_distributions.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Box Plots
print("Generating box plots...")
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for idx, feature in enumerate(features):
    axes[idx].boxplot(df[feature])
    axes[idx].set_title(f'{feature}')
    axes[idx].set_ylabel('Value')
    axes[idx].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(figures_dir / 'univariate_boxplots.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Q-Q Plots
print("Generating Q-Q plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
for idx, feature in enumerate(features):
    ax = axes[idx // 2, idx % 2]
    stats.probplot(df[feature], dist='norm', plot=ax)
    ax.set_title(f'Q-Q Plot: {feature}')
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(figures_dir / 'univariate_qqplots.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "=" * 80)
print("UNIVARIATE ANALYSIS COMPLETE! Results saved to results/figures/ directory")
print("=" * 80)

