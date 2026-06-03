import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/hdfc_top100_direct_nav.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True)

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["nav"])

plt.title("HDFC Top 100 Direct NAV")
plt.xlabel("Date")
plt.ylabel("NAV")

plt.grid(True)
plt.tight_layout()

plt.show()