"""
Rent Data Ingestion Script
NeighborWise AI

Purpose:
This script prepares the rent data ingestion layer.
For the MVP, it creates a sample rent dataset.
Later, this script can be updated to pull data from CMHC,
licensed rental APIs, or approved open data sources.
"""


from pathlib import Path
from datetime import datetime 

import pandas as pd



RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def create_sample_rent_data() -> pd.DataFrame:
    """
    Create sample rent data for the first MVP version.

    Later, this function will be replaced or extended with
    API calls or official data downloads.
    """

    rent_data = [
        {
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "rental_zone": "Kitchener Central",
            "property_type": "Apartment",
            "bedroom_type": "Studio",
            "average_rent": 1500,
            "rent_source_type": "Official Benchmark",
            "data_source": "CMHC",
            "report_year": 2025,
            "last_updated": datetime.today().date(),
        },
        {
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "rental_zone": "Kitchener Central",
            "property_type": "Apartment",
            "bedroom_type": "1 Bedroom",
            "average_rent": 1750,
            "rent_source_type": "Official Benchmark",
            "data_source": "CMHC",
            "report_year": 2025,
            "last_updated": datetime.today().date(),
        },
        {
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "rental_zone": "Kitchener Central",
            "property_type": "Apartment",
            "bedroom_type": "2 Bedroom",
            "average_rent": 2000,
            "rent_source_type": "Official Benchmark",
            "data_source": "CMHC",
            "report_year": 2025,
            "last_updated": datetime.today().date(),
        },
        {
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "rental_zone": "Kitchener Central",
            "property_type": "Apartment",
            "bedroom_type": "3 Bedroom+",
            "average_rent": 2125,
            "rent_source_type": "Official Benchmark",
            "data_source": "CMHC",
            "report_year": 2025,
            "last_updated": datetime.today().date(),
        },
    ]

    return pd.DataFrame(rent_data)


def save_rent_data(df: pd.DataFrame) -> None:
    """
    Save rent data to raw and processed folders.
    """

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    raw_file_path = RAW_DATA_DIR / "rent_data_raw.csv"
    processed_file_path = PROCESSED_DATA_DIR / "fact_rent.csv"

    df.to_csv(raw_file_path, index=False)
    df.to_csv(processed_file_path, index=False)

    print(f"Raw rent data saved to: {raw_file_path}")
    print(f"Processed rent data saved to: {processed_file_path}")


def main() -> None:
    rent_df = create_sample_rent_data()
    save_rent_data(rent_df)
    print("Rent data ingestion completed successfully.")


if __name__ == "__main__":
    main()