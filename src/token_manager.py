import requests
import logging
from src.config import (
    API_TOKEN_URL,
    REALM,
    CLIENT_ID,
    CLIENT_SECRET,
    SCOPES,
    CONTENT_TYPE,
    REQUEST_TIMEOUT,
)

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def get_bearer_token():
    """
    Generate a bearer token using client credentials.

    Returns:
        dict: A dictionary containing the access token and its metadata.
    """
    # Construct the full URL with the realm parameter
    url = f"{API_TOKEN_URL}?realm={REALM}"

    # Define the payload and headers
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": SCOPES,
    }
    headers = {
        "Content-Type": CONTENT_TYPE,
    }

    try:
        logger.info(f"Requesting bearer token from URL: {url}")
        response = requests.post(url, data=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP errors

        token_data = response.json()
        logger.info("Bearer token retrieved successfully.")
        return token_data

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to generate bearer token: {e}")
        logger.debug(f"Response content: {response.text if response else 'No response'}")
        raise