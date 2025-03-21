import pandas as pd

df = pd.read_csv('athletes.csv')

df['disciplines'] = df['disciplines'].str.strip("[]").str.replace("'", "")

disciplines_of_interest = ['Artistic Swimming', 'Marathon Swimming', 'Diving', 'Water Polo', 'Swimming', 'Surfing']
df_filtered = df[df['disciplines'].isin(disciplines_of_interest)]

df_filtered[['last_Name', 'first_Name']] = df_filtered['name'].str.extract(r'([A-Z\s]+)\s(.*)')

df_final = df_filtered[['code', 'first_Name', 'last_Name', 'gender', 'country_code', 'disciplines']]

df_final_sample = df_final.sample(n=200)

df_final_sample.to_csv('filtered_athletes.csv', index=False)

print("Filtered data has been saved to 'filtered_athletes.csv'.")
