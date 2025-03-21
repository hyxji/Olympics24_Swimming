import pandas as pd

# Step 1: Load the CSV files
teams_df = pd.read_csv('teams.csv')
disciplines_df = pd.read_csv('disciplines.csv')
events_df = pd.read_csv('filtered_events_with_event_id.csv')  # Load the events file

# Step 2: Filter teams based on disciplines of interest
disciplines_of_interest = ['Artistic Swimming', 'Marathon Swimming', 'Diving', 'Water Polo', 'Swimming', 'Surfing']
teams_filtered = teams_df[teams_df['discipline'].isin(disciplines_of_interest)]

# Step 3: Merge teams with disciplines to get the Discipline_Code
merged_df = teams_filtered.merge(disciplines_df, left_on='discipline', right_on='Discipline_Name', how='left')

# Debug: Check the columns after merging with disciplines_df
print("Columns after merging with disciplines_df:", merged_df.columns)

# Step 4: Merge with the events file to retrieve the Event_ID using the Event_Tag
final_df = merged_df.merge(events_df, left_on='events', right_on='Event_Tag', how='left')

# Debug: Check the columns after merging with events_df
print("Columns after merging with events_df:", final_df.columns)

# Step 5: Keep only the relevant columns and reorder them
try:
    df_final = final_df[['code', 'team', 'team_gender', 'country_code', 'Discipline_Code', 'Event_ID']]
except KeyError as e:
    print("Error selecting columns:", e)
    print("Available columns:", final_df.columns)
    raise

# Step 6: Rename columns to match the required names
df_final.columns = ['Team_Code', 'Team_Name', 'Team_Gender', 'Country_Code', 'Discipline_Code', 'Event_ID']

# Step 7: Save the final filtered data to a new CSV
df_final.to_csv('filtered_teams.csv', index=False)

print("Filtered team data has been saved to 'filtered_teams.csv'.")
