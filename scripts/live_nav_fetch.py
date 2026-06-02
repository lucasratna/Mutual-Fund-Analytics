import requests
import pandas as pd

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        "data/raw/hdfc_top100_direct_nav.csv",
        index=False
    )

    print("NAV data saved successfully!")
    print(nav_df.head())
else:
    print("API request failed:", response.status_code)