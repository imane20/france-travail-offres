import requests
import logging
from token_manager import get_bearer_token
from config import (
    JOB_OFFERS_URL,
    DEPARTMENT,
    CONTRACT_TYPE,
    REQUEST_TIMEOUT,
    LOG_LEVEL,
)

# Set up logging
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def fetch_offers(department=DEPARTMENT, contract_type=CONTRACT_TYPE):
    """
    Fetch job offers from the API using the Bearer token, filtered by department and contract type.

    Args:
        department (str): The department to filter job offers by.
        contract_type (str): The contract type to filter job offers by.

    Returns:
        dict: The API response containing job offers.
    """
    try:
        # Get the Bearer token
        token_info = get_bearer_token()
        access_token = token_info["access_token"]

        # Set up headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # Define query parameters
        params = {
            "departement": department,
            "typeContrat": contract_type,
        }

        logger.info(f"Fetching job offers from API: {JOB_OFFERS_URL} with filters: {params}")
        response = requests.get(JOB_OFFERS_URL, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # Raise exception for HTTP errors

        offers = response.json()
        logger.info(f"Successfully retrieved {len(offers.get('resultats', []))} job offers.")
        return offers

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch job offers: {e}")
        raise
