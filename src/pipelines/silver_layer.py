import os
import pandas as pd
import json
import logging
from datetime import datetime
from src.config import BRONZE_PATH, SILVER_PATH
from csv import QUOTE_ALL

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Helper to load raw data
def load_bronze_data():
    """
    Load the JSON data from the latest bronze directory.
    """
    today_date = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(BRONZE_PATH, today_date, "job_offers.json")
    
    logging.info(f"Loading data from {file_path}")
    
    if not os.path.exists(file_path):
        logging.error(f"File {file_path} not found.")
        raise FileNotFoundError(f"File {file_path} not found.")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    logging.info("Data loaded successfully")
    return pd.json_normalize(data)

# Extract and save the flattened offers table
def create_offers_csv(df):
    """
    Create the flattened offers table and save as CSV.
    """
    logging.info("Creating flattened offers table")
    flattened = pd.json_normalize(df.to_dict(orient="records"))
    flattened.columns = [col.replace('.', '_') for col in flattened.columns]
    today_date = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(SILVER_PATH, today_date, "offers.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    flattened.to_csv(output_path, index=False, sep=',', quotechar='"', quoting=QUOTE_ALL)
    logging.info(f"Offers CSV saved at {output_path}")

# Extract and save the entreprise table
def create_entreprise_csv(df):
    """
    Create the entreprise table with id and entreprise details.
    """
    logging.info("Creating entreprise table")
    entreprise_data = df[["id", "entreprise.nom", "entreprise.description", "entreprise.logo", 
                          "entreprise.url", "entreprise.entrepriseAdaptee"]].copy()
    entreprise_data.columns = ["id", "entreprise_nom", "entreprise_description", "entreprise_logo", 
                               "entreprise_url", "entreprise_entrepriseAdaptee"]
    today_date = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(SILVER_PATH, today_date, "entreprises.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    entreprise_data.to_csv(output_path, index=False, sep=',', quotechar='"', quoting=QUOTE_ALL)
    logging.info(f"Entreprise CSV saved at {output_path}")

# Extract and save the competences table
def create_competences_csv(df):
    """
    Create the competences table by exploding and flattening the competences array.
    """
    logging.info("Creating competences table")
    competences_data = df[["id", "competences"]].explode("competences").dropna(subset=["competences"])
    competences_flattened = pd.json_normalize(competences_data["competences"])
    competences_flattened["id"] = competences_data["id"].values
    competences_flattened = competences_flattened[["id", "code", "libelle", "exigence"]]
    competences_flattened.columns = ["id", "competences_code", "competences_libelle", "competences_exigence"]
    
    today_date = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(SILVER_PATH, today_date, "competences.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    competences_flattened.to_csv(output_path, index=False, sep=',', quotechar='"', quoting=QUOTE_ALL)
    logging.info(f"Competences CSV saved at {output_path}")

# Main execution
if __name__ == "__main__":
    logging.info("Starting the pipeline")
    
    # Load data from the bronze layer
    df_bronze = load_bronze_data()
    
    # Create and save the CSVs
    create_offers_csv(df_bronze)
    create_entreprise_csv(df_bronze)
    create_competences_csv(df_bronze)
    
    logging.info("Pipeline execution completed")
