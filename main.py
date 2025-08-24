from extract import extract_data
from transform import transform_data
from load import load_data
import logging

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s -%(message)s", handlers=[
            logging.FileHandler("etl.log"),
            logging.StreamHandler()
        ]
    )

    logging.info("Starting ETL process...")

    try:
        data = extract_data("data/sales.csv")
        logging.info(f"Extracted {len(data)} rows.")

        transformed_data = transform_data(data)
        logging.info("Transformation complete.")

        load_data(transformed_data, "data/processed_sales.csv")
        logging.info("Data loaded successfully.")

    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()