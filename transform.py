# transform.py

import pandas as pd

def transform_data(df):
    """
    Simple transformation function:
    - Fill missing values
    - Convert column names to lowercase
    """
    df = df.copy()
    # Fill missing numeric values with 0
    df.fillna(0, inplace=True)
    # Lowercase column names
    df.columns = [col.lower() for col in df.columns]
    print(f"Data transformed successfully\nRows: {df.shape[0]}\nColumns: {df.shape[1]}")
    return df
