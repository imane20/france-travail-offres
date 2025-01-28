import pytest
from unittest.mock import patch
from src.token_manager import get_bearer_token

@patch("requests.post")
def test_get_bearer_token(mock_post):
    mock_post.return_value.json.return_value = {"access_token": "test_token"}
    mock_post.return_value.status_code = 200

    token = get_bearer_token()
    assert token["access_token"] == "test_token"
