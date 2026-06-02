"""
School Data Ingestion Script
NeighborWise AI

Purpose:
This script prepares the school data layer.
For the MVP, it creates a sample school dataset.
Later, this script can be connected to official school data sources,
school board boundary data, and EQAO achievement results.
"""

from pathlib import Path
from datetime import datetime

import pandas as pd


RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def create_sample_school_data() -> pd.DataFrame:
    """
    Create sample school data for the first MVP version.

    Later, this function will be replaced or extended with
    official school APIs, open data files, or GIS boundary datasets.
    """

    school_data = [
        {
            "school_id": 1,
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "school_name": "King Edward Public School",
            "school_board": "WRDSB",
            "school_type": "Public",
            "grade_level": "Elementary",
            "address": "709 King St W, Kitchener, ON",
            "latitude": 43.4562,
            "longitude": -80.5054,
            "eqao_reading_score": 78,
            "eqao_writing_score": 80,
            "eqao_math_score": 74,
            "school_performance_score": 77.3,
            "data_source": "Sample - Replace with official source",
            "school_year": "2024-2025",
            "last_updated": datetime.today().date(),
        },
        {
            "school_id": 2,
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "school_name": "Suddaby Public School",
            "school_board": "WRDSB",
            "school_type": "Public",
            "grade_level": "Elementary",
            "address": "171 Frederick St, Kitchener, ON",
            "latitude": 43.4523,
            "longitude": -80.4864,
            "eqao_reading_score": 75,
            "eqao_writing_score": 76,
            "eqao_math_score": 72,
            "school_performance_score": 74.3,
            "data_source": "Sample - Replace with official source",
            "school_year": "2024-2025",
            "last_updated": datetime.today().date(),
        },
        {
            "school_id": 3,
            "city": "Kitchener",
            "neighborhood": "Downtown Kitchener",
            "school_name": "St. Teresa Catholic Elementary School",
            "school_board": "WCDSB",
            "school_type": "Catholic",
            "grade_level": "Elementary",
            "address": "270 Edwin St, Kitchener, ON",
            "latitude": 43.4641,
            "longitude": -80.5061,
            "eqao_reading_score": 82,
            "eqao_writing_score": 81,
            "eqao_math_score": 79,
            "school_performance_score": 80.7,
            "data_source": "Sample - Replace with official source",
            "school_year": "2024-2025",
            "last_updated": datetime.today().date(),
        },
    ]

    return pd.DataFrame(school_data)


def save_school_data(df: pd.DataFrame) -> None:
    """
    Save school data to raw and processed folders.
    """

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    raw_file_path = RAW_DATA_DIR / "school_data_raw.csv"
    processed_file_path = PROCESSED_DATA_DIR / "dim_school.csv"

    df.to_csv(raw_file_path, index=False)
    df.to_csv(processed_file_path, index=False)

    print(f"Raw school data saved to: {raw_file_path}")
    print(f"Processed school data saved to: {processed_file_path}")


def main() -> None:
    school_df = create_sample_school_data()
    save_school_data(school_df)
    print("School data ingestion completed successfully.")


if __name__ == "__main__":
    main()