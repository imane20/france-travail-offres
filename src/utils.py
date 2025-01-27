# utils.py

import pandas as pd

def rename_columns(df, rename_map):
    """
    Rename columns in a DataFrame based on a mapping.
    """
    return df.rename(columns=rename_map)

def cast_columns(df, columns, dtype):
    """
    Cast specified columns in a DataFrame to a given data type.
    """
    for column in columns:
        if column in df.columns:
            df[column] = df[column].astype(dtype)
    return df

def select_columns(df, columns):
    """
    Select and reorder columns in a DataFrame.
    """
    return df[columns]
