import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Database path
db_path = Path("data/db/bluestock_mf.db")

# Create SQLite connection
engine = create_engine(f"sqlite:///{db_path}")

# Processed data folder
processed_folder = Path("data/processed")

# Load all CSV files into SQLite
for csv_file in processed_folder.glob("*.csv"):
    table_name = csv_file.stem.lower()

    df = pd.read_csv(csv_file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {csv_file.name} -> {table_name}")

print("\nDatabase created successfully!")