import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

for table in tables["name"]:
    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM '{table}'",
        conn
    )
    print(table, ":", count["cnt"][0])

conn.close()