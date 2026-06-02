import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

for file in raw_path.glob("*.csv"):
    print(f"\nProcessing {file.name}")

    df = pd.read_csv(file)

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Duplicates removed: {before - after}")

    # Fill missing values
    df = df.fillna(method="ffill")

    # Save cleaned file
    output_file = processed_path / file.name
    df.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")

print("\nData cleaning completed!")