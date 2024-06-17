"""
Bivariate Analysis for Iris Dataset
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from itertools import combinations
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
print("BIVARIATE ANALYSIS - IRIS DATASET")
print("=" * 80)

# Create results directory
results_dir = Path(__file__).parent.parent.parent / 'results'
results_dir.mkdir(exist_ok=True)
figures_dir = results_dir / 'figures'
figures_dir.mkdir(exist_ok=True)

# 1. Correlation Analysis
print("\n1. CORRELATION ANALYSIS")
print("-" * 80)
pairs = list(combinations(features, 2))
print("\nPearson Correlation Coefficients:")
for f1, f2 in pairs:
    corr, p_value = pearsonr(df[f1], df[f2])
    print(f"  {f1} vs {f2}: r = {corr:.4f}, p-value = {p_value:.6f}")

# 2. Scatter Plots
print("\n2. GENERATING SCATTER PLOTS...")
print("-" * 80)
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()

for idx, (f1, f2) in enumerate(pairs):
    ax = axes[idx]
    for variety in df['variety'].unique():
        data = df[df['variety'] == variety]
        ax.scatter(data[f1], data[f2], label=variety, alpha=0.6)
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.set_title(f'{f1} vs {f2}')
    ax.legend()
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(figures_dir / 'bivariate_scatterplots.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Correlation Heatmap
print("Generating correlation heatmap...")
corr_matrix = df[features].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, square=True, 
            linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix', fontsize=16)
plt.tight_layout()
plt.savefig(figures_dir / 'bivariate_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Pair Plot
print("Generating pair plot...")
sns.pairplot(df, hue='variety', diag_kind='hist', height=2.5)
plt.suptitle('Pair Plot of Iris Dataset', y=1.02, fontsize=16)
plt.savefig(figures_dir / 'bivariate_pairplot.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "=" * 80)
print("BIVARIATE ANALYSIS COMPLETE! Results saved to results/figures/ directory")
print("=" * 80)

