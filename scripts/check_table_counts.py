import sqlite3

print("SCRIPT UPDATED VERSION RUNNING")

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("TABLE NAME → ROW COUNT\n")

for table in tables:
    table_name = table[0]

    cursor.execute(f'SELECT COUNT(*) FROM "{table_name}"')
    count = cursor.fetchone()[0]

    print(f"{table_name} → {count}")

conn.close()