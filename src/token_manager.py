import os
import requests
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configuration from .env
TOKEN_URL = os.getenv("API_TOKEN_URL")
REALM = os.getenv("REALM")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SCOPES = os.getenv("SCOPES")
CONTENT_TYPE = os.getenv("CONTENT_TYPE")

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def get_bearer_token():
    """
    Generate a bearer token using client credentials.
    """
    # Construct the full URL with the realm parameter
    url = f"{TOKEN_URL}?realm={REALM}"

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
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        token_data = response.json()
        logger.info("Bearer token retrieved successfully.")
        return token_data

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to generate bearer token: {e}")
        logger.debug(f"Response content: {response.text if response else 'No response'}")
        raise
