# Unicorn Companies Data Analysis Project

A comprehensive data science project analyzing unicorn companies (privately held startup companies valued at over $1 billion). This project includes exploratory data analysis, statistical analysis, univariate/bivariate/multivariate analysis, and machine learning models in both Python and R.

## 📊 Project Overview

This project provides a complete analysis pipeline for the Unicorn Companies dataset, including:
- **Exploratory Data Analysis (EDA)** - Data cleaning, visualization, and initial insights
- **Statistical Analysis** - Descriptive, inferential, and exploratory statistics
- **Univariate, Bivariate, and Multivariate Analysis** - Comprehensive relationship analysis
- **Machine Learning** - Regression and classification models

## 📁 Project Structure

```
Unicorn_Companies/
│
├── data/
│   ├── Unicorn_Companies.csv              # Original dataset
│   └── Unicorn_Companies_cleaned.csv      # Cleaned dataset (generated)
│
├── notebooks/
│   ├── python/
│   │   ├── 01_EDA_Unicorn_Companies.ipynb
│   │   ├── 02_Statistical_Analysis.ipynb
│   │   ├── 03_Univariate_Bivariate_Multivariate_Analysis.ipynb
│   │   └── 04_ML_Analysis.ipynb
│   │
│   └── r/
│       ├── 01_EDA_Unicorn_Companies.Rmd
│       ├── 02_Statistical_Analysis.Rmd
│       ├── 03_Univariate_Bivariate_Multivariate_Analysis.Rmd
│       └── 04_ML_Analysis.Rmd
│
├── scripts/
│   ├── python/
│   │   ├── eda.py
│   │   └── univariate_bivariate_multivariate_analysis.py
│   │
│   └── r/
│
├── results/
│   ├── models/                            # Saved ML models
│   └── plots/                             # Generated visualizations
│
├── docs/                                  # Documentation
│
├── requirements.txt                       # Python dependencies
├── environment.yml                        # Conda environment
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ or R 4.0+
- Jupyter Notebook or RStudio
- Git

### Installation

#### Python Environment

1. Clone the repository:
```bash
git clone <repository-url>
cd Unicorn_Companies
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using conda:
```bash
conda env create -f environment.yml
conda activate unicorn-companies
```

#### R Environment

1. Install required R packages:
```r
install.packages(c("dplyr", "ggplot2", "tidyr", "readr", "caret", 
                   "randomForest", "xgboost", "e1071", "knitr", 
                   "rmarkdown", "corrplot", "GGally"))
```

## 📖 Usage

### Python Analysis

#### Running Jupyter Notebooks

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to `notebooks/python/` and open notebooks in order:
   - `01_EDA_Unicorn_Companies.ipynb`
   - `02_Statistical_Analysis.ipynb`
   - `03_Univariate_Bivariate_Multivariate_Analysis.ipynb`
   - `04_ML_Analysis.ipynb`

#### Running Python Scripts

```bash
# Run EDA script
python scripts/python/eda.py

# Run univariate/bivariate/multivariate analysis
python scripts/python/univariate_bivariate_multivariate_analysis.py
```

### R Analysis

#### Running R Markdown Notebooks

1. Open RStudio
2. Open `.Rmd` files from `notebooks/r/` directory
3. Click "Knit" to render HTML reports

Or from R console:
```r
rmarkdown::render("notebooks/r/01_EDA_Unicorn_Companies.Rmd")
```

## 📈 Analysis Components

### 1. Exploratory Data Analysis (EDA)

- Data loading and inspection
- Missing value analysis
- Data cleaning and preprocessing
- Basic statistical summaries
- Initial visualizations

### 2. Statistical Analysis

- **Descriptive Statistics**: Mean, median, standard deviation, skewness, kurtosis
- **Inferential Statistics**: Hypothesis testing, confidence intervals
- **Correlation Analysis**: Pearson and Spearman correlations
- **Hypothesis Tests**: t-tests, ANOVA, Chi-square tests

### 3. Univariate, Bivariate, and Multivariate Analysis

- **Univariate**: Distribution analysis, normality tests, Q-Q plots
- **Bivariate**: Relationship analysis between pairs of variables
- **Multivariate**: Correlation matrices, heatmaps, pair plots, 3D scatter plots

### 4. Machine Learning Analysis

#### Regression Models (Predict Valuation)
- Random Forest Regressor
- XGBoost Regressor
- Linear Regression

#### Classification Models (Predict Financial Stage)
- Random Forest Classifier
- XGBoost Classifier
- Logistic Regression

#### Model Evaluation
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Classification reports
- Confusion matrices
- Feature importance analysis

## 🔍 Key Findings

(To be updated after running analyses)

## 📊 Dataset Information

### Dataset Columns

- **Company**: Company name
- **Valuation ($B)**: Company valuation in billions of USD
- **Date Joined**: Date when company reached unicorn status
- **Country**: Company's country
- **City**: Company's city
- **Industry**: Industry sector
- **Select Investors**: Key investors
- **Founded Year**: Year company was founded
- **Total Raised**: Total funding raised
- **Financial Stage**: Current financial stage (IPO, Acquired, etc.)
- **Investors Count**: Number of investors
- **Deal Terms**: Number of deal terms
- **Portfolio Exits**: Number of portfolio exits

### Dataset License

The Unicorn Companies dataset is used for educational and research purposes. Please refer to the original data source for dataset-specific licensing terms. If you use this dataset, please cite the original source appropriately.

**Important**: This project respects the original dataset's license. Users are responsible for ensuring they have the right to use the dataset according to its original license terms.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The dataset used in this project may have its own licensing terms. Please refer to the original data source for dataset-specific licensing information.

## 🙏 Acknowledgments

- Dataset source: [Original Data Source]
- Libraries and tools: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, R tidyverse, caret, randomForest

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

## 🗺️ Roadmap

- [ ] Add more advanced ML models
- [ ] Implement time series analysis
- [ ] Add interactive visualizations
- [ ] Create deployment pipeline
- [ ] Add unit tests
- [ ] Expand documentation

---

**Note**: This project is for educational purposes. Always verify and validate results before making business decisions based on this analysis.

---
*Enhanced with unicorn company analytics including funding trends and valuation modeling*

**Last Updated**: June 2024
