import pandas as pd

print("CLEANING STARTED")

# NAV HISTORY
nav = pd.read_csv("data/raw/nav_history.csv")

nav['date'] = pd.to_datetime(nav['date'], errors='coerce')
nav = nav.sort_values(['amfi_code', 'date'])
nav = nav.drop_duplicates()
nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()
nav = nav[nav['nav'] > 0]

nav.to_csv("data/processed/nav_history_cleaned.csv", index=False)
print("NAV CLEANED:", nav.shape)

# TRANSACTIONS
txn = pd.read_csv("data/raw/investor_transactions.csv")

txn['transaction_type'] = txn['transaction_type'].str.upper()
txn['amount'] = pd.to_numeric(txn['amount'], errors='coerce')
txn['date'] = pd.to_datetime(txn['date'], errors='coerce')
txn = txn[txn['amount'] > 0]

txn.to_csv("data/processed/investor_transactions_cleaned.csv", index=False)
print("TRANSACTIONS CLEANED:", txn.shape)

# PERFORMANCE
perf = pd.read_csv("data/raw/scheme_performance.csv")

perf['returns'] = pd.to_numeric(perf['returns'], errors='coerce')
perf = perf[(perf['expense_ratio'] >= 0.1) & (perf['expense_ratio'] <= 2.5)]

perf.to_csv("data/processed/scheme_performance_cleaned.csv", index=False)
print("PERFORMANCE CLEANED:", perf.shape)

print("ALL CLEANING DONE")