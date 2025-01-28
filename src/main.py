import logging
from src.token_manager import get_bearer_token
from src.api_client import fetch_all_offers
from src.pipelines.bronze_layer import save_raw_data
from src.pipelines.silver_layer import run_silver_pipeline
from src.pipelines.gold_layer import run_gold_pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    try:
        # Step 1: Get bearer token (for logging purposes)
        logger.info("Starting pipeline execution...")
        token = get_bearer_token()
        logger.info(f"Bearer token retrieved successfully: {token['access_token']}")

        # Step 2: Fetch job offers and save raw data in the bronze layer
        logger.info("Executing Bronze Layer...")
        save_raw_data()

        # Step 3: Process data in the silver layer
        logger.info("Executing Silver Layer...")
        run_silver_pipeline()

        # Step 4: Process data in the gold layer
        logger.info("Executing Gold Layer...")
        run_gold_pipeline()

        logger.info("Pipeline executed successfully!")

    except Exception as e:
        logger.error(f"An error occurred during pipeline execution: {e}")
        raise

if __name__ == "__main__":
    main()
