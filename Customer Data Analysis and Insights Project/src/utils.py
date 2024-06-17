"""
Utility functions for data analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


def get_project_paths():
    """
    Return project data/results paths resolved from this module's location.
    Works regardless of the current working directory.
    """
    data_dir = PROJECT_ROOT / 'data'
    results_dir = PROJECT_ROOT / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)
    return {
        'project_root': PROJECT_ROOT,
        'data_dir': data_dir,
        'results_dir': results_dir,
        'customers_csv': data_dir / 'Customers.csv',
    }


def load_data(data_path=None):
    """
    Load dataset from CSV file
    
    Parameters:
    -----------
    data_path : str or Path, optional
        Path to the CSV file. Defaults to project data/Customers.csv.
    
    Returns:
    --------
    pd.DataFrame
        Loaded dataset
    """
    if data_path is None:
        data_path = get_project_paths()['customers_csv']
    return pd.read_csv(data_path)

def save_results(data, output_path, filename):
    """
    Save analysis results to file
    
    Parameters:
    -----------
    data : pd.DataFrame or dict
        Data to save
    output_path : str or Path
        Output directory path
    filename : str
        Output filename
    """
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    
    if isinstance(data, pd.DataFrame):
        data.to_csv(output_path / filename, index=False)
    else:
        import json
        with open(output_path / filename, 'w') as f:
            json.dump(data, f, indent=2)

def get_data_summary(df):
    """
    Get summary statistics for the dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    
    Returns:
    --------
    dict
        Summary statistics
    """
    return {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'duplicate_count': df.duplicated().sum()
    }


if __name__ == "__main__":
    paths = get_project_paths()
    print("Project root:", paths['project_root'])
    print("Data file:", paths['customers_csv'])
    print("Exists:", paths['customers_csv'].exists())
    df = load_data()
    summary = get_data_summary(df)
    print("Shape:", summary['shape'])
    print("Columns:", summary['columns'])
    print("utils.py OK")
