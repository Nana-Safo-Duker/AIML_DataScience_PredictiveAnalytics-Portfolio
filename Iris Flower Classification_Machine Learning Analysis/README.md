# Iris Dataset - Comprehensive Data Science Analysis

A comprehensive data science project analyzing the famous Iris dataset with exploratory data analysis, statistical analysis, univariate/bivariate/multivariate analysis, and machine learning implementations in both Python and R.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Components](#analysis-components)
- [Results](#results)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🎯 Project Overview

This project provides a complete data science workflow for the Iris dataset, including:

1. **Exploratory Data Analysis (EDA)** - Comprehensive data exploration and visualization
2. **Statistical Analysis** - Descriptive, inferential, and exploratory statistical analysis
3. **Univariate Analysis** - Analysis of individual features
4. **Bivariate Analysis** - Analysis of relationships between feature pairs
5. **Multivariate Analysis** - Dimensionality reduction and multivariate techniques
6. **Machine Learning** - Implementation of multiple classification algorithms

All analyses are implemented in both **Python** and **R** for maximum flexibility.

## 📊 Dataset Information

### Dataset Description

The Iris dataset is one of the most famous datasets in pattern recognition literature. It contains measurements of 150 iris flowers from three different species:

- **Setosa** (50 samples)
- **Versicolor** (50 samples)
- **Virginica** (50 samples)

### Features

Each sample has four features:

1. **Sepal Length** (cm) - `sepal.length`
2. **Sepal Width** (cm) - `sepal.width`
3. **Petal Length** (cm) - `petal.length`
4. **Petal Width** (cm) - `petal.width`

### Target Variable

- **Variety** - The species of iris (Setosa, Versicolor, or Virginica)

### Dataset License

The Iris dataset is in the public domain and is freely available for use. It was introduced by Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" and has since become a standard dataset in machine learning and statistics.

**Original Source:** Fisher, R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936)

**Current Source:** The dataset is widely available and can be found in various repositories including:
- UCI Machine Learning Repository
- scikit-learn datasets
- R datasets package

This dataset is provided for educational and research purposes. No copyright restrictions apply.

## 📁 Project Structure

```
Iris/
├── data/
│   └── Iris.csv                 # Dataset file
├── notebooks/
│   ├── python/
│   │   ├── 01_EDA.ipynb         # Exploratory Data Analysis
│   │   ├── 02_Statistical_Analysis.ipynb
│   │   ├── 03_Univariate_Analysis.ipynb
│   │   ├── 04_Bivariate_Analysis.ipynb
│   │   ├── 05_Multivariate_Analysis.ipynb
│   │   └── 06_ML_Analysis.ipynb # Machine Learning Analysis
│   └── r/
│       ├── 01_EDA.Rmd           # Exploratory Data Analysis (R)
│       ├── 02_Statistical_Analysis.Rmd
│       ├── 03_Univariate_Analysis.Rmd
│       ├── 04_Bivariate_Analysis.Rmd
│       ├── 05_Multivariate_Analysis.Rmd
│       └── 06_ML_Analysis.Rmd   # Machine Learning Analysis (R)
├── scripts/
│   ├── python/
│   │   ├── eda.py               # EDA script
│   │   ├── univariate_analysis.py
│   │   ├── bivariate_analysis.py
│   │   └── multivariate_analysis.py
│   └── r/
│       └── (R scripts can be added here)
├── results/
│   ├── figures/                 # Generated visualizations
│   └── tables/                  # Generated tables
├── models/                      # Saved models
├── docs/                        # Additional documentation
├── requirements.txt             # Python dependencies
├── requirements_r.txt           # R dependencies
├── .gitignore
└── README.md                    # This file
```

## 🔧 Installation

### Python Environment

1. Clone the repository:
```bash
git clone <repository-url>
cd Iris
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### R Environment

1. Install R and RStudio (if not already installed)

2. Install R packages:
```r
# Open R or RStudio and run:
install.packages(c("dplyr", "tidyr", "readr", "ggplot2", "gridExtra", 
                   "corrplot", "ggcorrplot", "RColorBrewer", "psych", 
                   "DescTools", "car", "caret", "randomForest", "e1071", 
                   "nnet", "rpart", "knitr", "rmarkdown", "FactoMineR", 
                   "factoextra"))
```

## 📖 Usage

### Python Notebooks

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to `notebooks/python/` and open the desired notebook:
   - `01_EDA.ipynb` - Start here for exploratory data analysis
   - `02_Statistical_Analysis.ipynb` - Statistical tests and analysis
   - `03_Univariate_Analysis.ipynb` - Individual feature analysis
   - `04_Bivariate_Analysis.ipynb` - Pairwise feature analysis
   - `05_Multivariate_Analysis.ipynb` - Dimensionality reduction
   - `06_ML_Analysis.ipynb` - Machine learning models

### Python Scripts

Run analysis scripts directly:
```bash
python scripts/python/eda.py
python scripts/python/univariate_analysis.py
python scripts/python/bivariate_analysis.py
python scripts/python/multivariate_analysis.py
```

### R Notebooks

1. Open RStudio

2. Open the desired `.Rmd` file from `notebooks/r/`

3. Click "Knit" to render the notebook to HTML

Alternatively, render from command line:
```r
rmarkdown::render("notebooks/r/01_EDA.Rmd")
```

## 📈 Analysis Components

### 1. Exploratory Data Analysis (EDA)

- Dataset overview and structure
- Data quality checks (missing values, duplicates)
- Descriptive statistics
- Data visualizations (histograms, box plots, pair plots)
- Outlier detection
- Correlation analysis

### 2. Statistical Analysis

- **Descriptive Statistics**: Mean, median, standard deviation, skewness, kurtosis
- **Inferential Statistics**: 
  - One-way ANOVA
  - Pairwise t-tests
  - Normality tests (Shapiro-Wilk)
  - Kruskal-Wallis test (non-parametric)
- **Confidence Intervals**: 95% confidence intervals for means
- **Effect Size**: Cohen's d for effect size measurement

### 3. Univariate Analysis

- Distribution analysis for each feature
- Histograms and density plots
- Box plots
- Q-Q plots for normality assessment
- Statistical measures for each variable

### 4. Bivariate Analysis

- Scatter plots between feature pairs
- Correlation analysis (Pearson and Spearman)
- Correlation heatmaps
- Pair plots
- Relationship visualization by species

### 5. Multivariate Analysis

- **Principal Component Analysis (PCA)**:
  - Dimensionality reduction
  - Explained variance analysis
  - PCA visualization
  - Feature contribution to principal components
  - Scree plots

### 6. Machine Learning Analysis

Implementation of multiple classification algorithms:

- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Decision Tree**
- **Random Forest**
- **Gradient Boosting**
- **k-Nearest Neighbors (KNN)**
- **Naive Bayes**

Each model includes:
- Training and testing
- Cross-validation
- Performance metrics (accuracy, precision, recall, F1-score)
- Confusion matrices
- Feature importance (where applicable)
- Model comparison

## 📊 Results

### Key Findings

1. **Data Quality**: The dataset is clean with no missing values and balanced classes (50 samples per species)

2. **Feature Relationships**: 
   - Strong positive correlation between petal length and petal width (r > 0.9)
   - Moderate correlations between sepal and petal measurements

3. **Class Separability**:
   - Setosa is linearly separable from other classes
   - Versicolor and Virginica show some overlap but are distinguishable

4. **Statistical Significance**: All features show significant differences between species (ANOVA p < 0.05)

5. **Machine Learning Performance**: Multiple algorithms achieve high accuracy (>95%), with Random Forest and SVM typically performing best

### Generated Outputs

All analysis results are saved in the `results/` directory:
- Figures: `results/figures/`
- Tables: `results/tables/`
- Models: `models/`

## 📝 License

### Dataset License

The Iris dataset is in the public domain and is freely available for educational and research purposes. No copyright restrictions apply.

**Original Work**: Fisher, R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936)

### Project License

This project and its code are provided as-is for educational and research purposes. Feel free to use, modify, and distribute according to your needs.

## 🙏 Acknowledgments

- **Ronald Fisher** - For introducing the Iris dataset in 1936
- **UCI Machine Learning Repository** - For maintaining and providing access to the dataset
- **scikit-learn** - For Python machine learning tools
- **R Community** - For comprehensive statistical and machine learning packages
- **Open Source Community** - For the amazing tools and libraries that made this project possible

## 📚 References

1. Fisher, R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936)

2. Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

3. Pedregosa et al., "Scikit-learn: Machine Learning in Python", JMLR 12, pp. 2825-2830, 2011.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or suggestions, please open an issue on the repository.

---

**Note**: This project is intended for educational purposes and serves as a comprehensive example of data science workflow from exploration to machine learning.

---
*Enhanced with Iris classification ML workflow including visualizations and model comparisons*

**Last Updated**: June 2024
