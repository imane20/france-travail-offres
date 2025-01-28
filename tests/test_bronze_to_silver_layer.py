import os
import json
import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.pipelines.silver_layer import load_bronze_data, create_offers_csv
from src.config import BRONZE_PATH, SILVER_PATH

@pytest.fixture
def mock_json_load():
    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps([{"id": "1"}])
        yield mock_open

@patch("builtins.open", new_callable=MagicMock)
@patch("os.path.exists", return_value=True)
def test_load_bronze_data(mock_exists, mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = json.dumps([{"id": "1"}])
    today_date = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(BRONZE_PATH, today_date, "job_offers.json")

    df = load_bronze_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    mock_open.assert_called_once_with(file_path, "r", encoding="utf-8")

@patch("pandas.DataFrame.to_csv")
def test_create_offers_csv(mock_to_csv):
    df = pd.DataFrame([{"id": "1", "intitule": "Test"}])
    create_offers_csv(df)

    mock_to_csv.assert_called_once()
