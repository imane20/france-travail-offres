import os
import pandas as pd
import logging
from datetime import datetime
from src.config import SILVER_PATH, GOLD_PATH, \
    COLUMN_RENAME_OFFERS, \
    STRING_COLUMNS_OFFERS, \
    BOOLEAN_COLUMNS_OFFERS, \
    INTEGER_COLUMNS_OFFERS, \
    DOUBLE_COLUMNS_OFFERS, \
    DATE_COLUMNS_OFFERS, \
    SELECT_COLUMNS_OFFERS, \
    COLUMN_RENAME_ENTREPRISES, \
    STRING_COLUMNS_ENTREPRISES, \
    BOOLEAN_COLUMNS_ENTREPRISES, \
    SELECT_COLUMNS_ENTREPRISES, \
    COLUMN_RENAME_COMPETENCES, \
    STRING_COLUMNS_COMPETENCES, \
    SELECT_COLUMNS_COMPETENCES
from src.utils import rename_columns, cast_columns, select_columns

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Paths
today_date = datetime.now().strftime("%Y-%m-%d")
silver_path = os.path.join(SILVER_PATH, today_date)
gold_path = os.path.join(GOLD_PATH, today_date)

# Ensure gold path exists
os.makedirs(gold_path, exist_ok=True)

def process_table(input_file, output_file, rename_map, string_cols, bool_cols, int_cols, float_cols, date_cols, select_cols):
    """
    Generic function to process a table and save it to the gold layer.
    """
    logger.info(f"Processing table: {input_file}")
    file_path = os.path.join(silver_path, input_file)
    
    if not os.path.exists(file_path):
        logger.error(f"{file_path} does not exist.")
        return
    
    df = pd.read_csv(file_path)
    logger.info(f"Initial row count: {len(df)}")
    
    # Rename columns
    df = rename_columns(df, rename_map)
    
    # Cast columns to the correct types
    df = cast_columns(df, string_cols, "string")
    df = cast_columns(df, bool_cols, "boolean")
    df = cast_columns(df, int_cols, "int32")
    df = cast_columns(df, float_cols, "float64")
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    
    # Select and reorder columns
    df = select_columns(df, select_cols)
    
    # Drop duplicates and log counts
    before_distinct = len(df)
    df.drop_duplicates(inplace=True)
    after_distinct = len(df)
    logger.info(f"Row count before distinct: {before_distinct}, after distinct: {after_distinct}")
    
    # Save the processed table
    output_path = os.path.join(gold_path, output_file)
    df.to_csv(output_path, index=False)
    logger.info(f"Table saved to {output_path}")

def process_offers_table():
    """
    Process the offers table.
    """
    process_table(
        input_file="offers.csv",
        output_file="gold_offres.csv",
        rename_map=COLUMN_RENAME_OFFERS,
        string_cols=STRING_COLUMNS_OFFERS,
        bool_cols=BOOLEAN_COLUMNS_OFFERS,
        int_cols=INTEGER_COLUMNS_OFFERS,
        float_cols=DOUBLE_COLUMNS_OFFERS,
        date_cols=DATE_COLUMNS_OFFERS,
        select_cols=SELECT_COLUMNS_OFFERS,
    )

def process_entreprises_table():
    """
    Process the entreprises table.
    """
    process_table(
        input_file="entreprises.csv",
        output_file="gold_entreprises.csv",
        rename_map=COLUMN_RENAME_ENTREPRISES,
        string_cols=STRING_COLUMNS_ENTREPRISES,
        bool_cols=BOOLEAN_COLUMNS_ENTREPRISES,
        int_cols=[],
        float_cols=[],
        date_cols=[],
        select_cols=SELECT_COLUMNS_ENTREPRISES,
    )

def process_competences_table():
    """
    Process the competences table.
    """
    process_table(
        input_file="competences.csv",
        output_file="gold_competences.csv",
        rename_map=COLUMN_RENAME_COMPETENCES,
        string_cols=STRING_COLUMNS_COMPETENCES,
        bool_cols=[],
        int_cols=[],
        float_cols=[],
        date_cols=[],
        select_cols=SELECT_COLUMNS_COMPETENCES,
    )

if __name__ == "__main__":
    logger.info("Starting gold layer processing")
    process_offers_table()
    process_entreprises_table()
    process_competences_table()
    logger.info("Gold layer processing completed")
