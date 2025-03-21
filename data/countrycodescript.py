import pandas as pd

df = pd.read_csv('filtered_athletes.csv')

unique_country_codes = df['country_code'].unique()

with open('unique_country_codes.txt', 'w') as f:
    for code in unique_country_codes:
        f.write(f"{code}\n")

print("Unique country codes have been saved to 'unique_country_codes.txt'.")
