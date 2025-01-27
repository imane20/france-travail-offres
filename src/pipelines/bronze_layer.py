import os
import json
from datetime import datetime
import logging
from src.api_client import fetch_all_offers
from src.config import BRONZE_PATH, DEPARTMENT, CONTRACT_TYPE, LOG_LEVEL

# Configure logging
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def save_raw_data():
    """
    Fetch all job offers using the API client and save them to a JSON file
    in the bronze layer directory with today's date as a subdirectory.
    """
    try:
        # Fetch all job offers
        all_offers = fetch_all_offers(department=DEPARTMENT, contract_type=CONTRACT_TYPE)
        total_offers = len(all_offers)  # Total number of offers retrieved

        # Get today's date in YYYY-MM-DD format
        today_date = datetime.now().strftime("%Y-%m-%d")

        # Create the output directory
        output_dir = os.path.join(BRONZE_PATH, today_date)
        os.makedirs(output_dir, exist_ok=True)

        # Define the output file path
        output_file = os.path.join(output_dir, "job_offers.json")

        # Save the data to a JSON file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_offers, f, indent=4, ensure_ascii=False)

        logger.info(f"Raw data successfully saved to: {output_file}")
        logger.info(f"Successfully retrieved {total_offers} job offers.")

    except Exception as e:
        logger.error(f"An error occurred while fetching or saving job offers: {e}")
        raise


if __name__ == "__main__":
    save_raw_data()
