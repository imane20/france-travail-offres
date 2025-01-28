import os
import pandas as pd
import pytest
from unittest.mock import patch
from src.pipelines.gold_layer import process_offers_table
from src.config import SILVER_PATH, SELECT_COLUMNS_OFFERS

@patch("pandas.read_csv")
@patch("pandas.DataFrame.to_csv")
def test_process_offers_table(mock_to_csv, mock_read_csv):
    # Create mocked data with correct types for each column
    mock_data = {col: "test_value" for col in SELECT_COLUMNS_OFFERS}
    
    # Correctly mock boolean columns with True/False
    for col in ["accessible_th", "alternance", "offres_manque_candidats"]:  # BOOLEAN_COLUMNS_OFFERS
        if col in mock_data:
            mock_data[col] = True

    # Correctly mock numeric columns
    for col in ["lieu_travail_latitude", "lieu_travail_longitude"]:  # DOUBLE_COLUMNS_OFFERS
        if col in mock_data:
            mock_data[col] = 12.345

    # Correctly mock integer columns
    for col in ["nombre_postes"]:  # INTEGER_COLUMNS_OFFERS
        if col in mock_data:
            mock_data[col] = 5

    # Correctly mock datetime columns
    for col in ["date_creation", "date_actualisation"]:  # DATE_COLUMNS_OFFERS
        if col in mock_data:
            mock_data[col] = "2023-01-01T00:00:00Z"

    # Mock DataFrame
    mock_read_csv.return_value = pd.DataFrame([mock_data])

    # Call the function
    process_offers_table()

    # Verify that the DataFrame was saved to a CSV
    mock_to_csv.assert_called_once()