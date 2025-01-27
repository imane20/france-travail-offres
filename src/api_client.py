import requests
import logging
from src.token_manager import get_bearer_token
from src.config import JOB_OFFERS_URL, REQUEST_TIMEOUT

logger = logging.getLogger(__name__)

def fetch_single_page(department, contract_type, range_start, range_end):
    """
    Fetch a single page of job offers from the API.
    Args:
        department (str): Department filter.
        contract_type (str): Contract type filter.
        range_start (int): Start index of the range.
        range_end (int): End index of the range.
    Returns:
        dict: The JSON response from the API and the Content-Range header.
    """
    try:
        # Set up headers and parameters
        headers = {
            "Authorization": f"Bearer {get_bearer_token()['access_token']}",
            "Content-Type": "application/json",
            "Range": f"offres {range_start}-{range_end}"
        }
        params = {
            "departement": department,
            "typeContrat": contract_type,
        }

        logger.info(f"Fetching offers with range {range_start}-{range_end}")
        response = requests.get(JOB_OFFERS_URL, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        return {
            "data": response.json(),
            "content_range": response.headers.get("Content-Range", "")
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch offers: {e}")
        raise

def fetch_all_offers(department, contract_type, range_step=150):
    """
    Fetch all job offers from the API using pagination.
    Args:
        department (str): Department filter.
        contract_type (str): Contract type filter.
        range_step (int): Number of offers to fetch per request.
    Returns:
        list: A combined list of all job offers.
    """
    all_offers = []
    range_start = 0

    while True:
        # Calculate the end of the current range
        range_end = range_start + range_step - 1

        # Fetch a single page of data
        result = fetch_single_page(department, contract_type, range_start, range_end)
        offers = result["data"].get("resultats", [])
        all_offers.extend(offers)

        # Parse Content-Range header
        content_range = result["content_range"]
        if not content_range:
            break  # Exit if Content-Range is missing
        total_offers = int(content_range.split("/")[-1])

        # Break when all offers are fetched
        if range_end + 1 >= total_offers:
            break

        # Increment range_start for the next page
        range_start += range_step

    return all_offers
