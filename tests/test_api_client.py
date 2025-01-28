import pytest
from unittest.mock import patch
from src.api_client import fetch_all_offers

@patch("src.api_client.fetch_single_page")
def test_fetch_all_offers(mock_fetch_single_page):
    mock_fetch_single_page.return_value = {
        "data": {"resultats": [{"id": "1"}]},
        "content_range": "0-1/1"
    }

    results = fetch_all_offers("07", "CDI")
    assert len(results) == 1
    assert results[0]["id"] == "1"
