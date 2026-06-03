import requests
import pandas as pd

# HDFC Top 100 Direct
url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

nav_df = pd.DataFrame(data["data"])

# Save raw data
nav_df.to_csv("data/raw/hdfc_top100_live_nav.csv", index=False)

print(nav_df.head())
print("Live NAV data saved successfully!")