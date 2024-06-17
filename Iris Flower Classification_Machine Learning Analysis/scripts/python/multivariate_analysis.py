"""
Multivariate Analysis for Iris Dataset
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
np.random.seed(42)

# Load data
data_path = Path(__file__).parent.parent.parent / 'data' / 'Iris.csv'
df = pd.read_csv(data_path)
features = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
X = df[features]
y = df['variety']

print("=" * 80)
print("MULTIVARIATE ANALYSIS - IRIS DATASET")
print("=" * 80)

# Create results directory
results_dir = Path(__file__).parent.parent.parent / 'results'
results_dir.mkdir(exist_ok=True)
figures_dir = results_dir / 'figures'
figures_dir.mkdir(exist_ok=True)

# 1. Principal Component Analysis
print("\n1. PRINCIPAL COMPONENT ANALYSIS (PCA)")
print("-" * 80)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Explained variance
print("\nExplained Variance Ratio:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")

print(f"\nTotal variance explained by first 2 components: {sum(pca.explained_variance_ratio_[:2]):.4f} ({sum(pca.explained_variance_ratio_[:2])*100:.2f}%)")

# 2. PCA Visualization
print("\n2. GENERATING PCA VISUALIZATIONS...")
print("-" * 80)

# Create DataFrame with PCA results
df_pca = pd.DataFrame(X_pca[:, :2], columns=['PC1', 'PC2'])
df_pca['variety'] = y

# Plot PCA results
plt.figure(figsize=(10, 8))
for variety in df_pca['variety'].unique():
    data = df_pca[df_pca['variety'] == variety]
    plt.scatter(data['PC1'], data['PC2'], label=variety, alpha=0.7, s=100)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.2f}% variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.2f}% variance)')
plt.title('PCA: First Two Principal Components')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(figures_dir / 'multivariate_pca.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Feature Contribution to Principal Components
print("\n3. FEATURE CONTRIBUTION TO PRINCIPAL COMPONENTS")
print("-" * 80)
pca_components = pd.DataFrame(
    pca.components_.T,
    columns=[f'PC{i+1}' for i in range(len(features))],
    index=features
)
print(pca_components.round(4))

# 4. Scree Plot
print("\n4. GENERATING SCREE PLOT...")
print("-" * 80)
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), 
         pca.explained_variance_ratio_, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Scree Plot')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(figures_dir / 'multivariate_scree_plot.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "=" * 80)
print("MULTIVARIATE ANALYSIS COMPLETE! Results saved to results/figures/ directory")
print("=" * 80)

