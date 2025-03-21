import pandas as pd

venues_df = pd.read_csv('venues.csv')

filtered_venues_df = venues_df[['venue', 'date_start', 'date_end']]

filtered_venues_df.to_csv('filtered_venues.csv', index=False)

print("Filtered venues saved to 'filtered_venues.csv'.")
