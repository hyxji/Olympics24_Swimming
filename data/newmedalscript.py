import pandas as pd

df_medals = pd.read_csv('filtered_medals.csv')
df_events = pd.read_csv('filtered_events_with_event_id.csv')
df_athletes = pd.read_csv('athletes.csv')

df_medals_athlete = df_medals[df_medals['Athlete_Code'].isin(df_athletes['code'])]

df_merged = pd.merge(df_medals_athlete, df_events[['Event_ID', 'Event_Tag']], on='Event_Tag', how='inner')

df_final = df_merged[['Athlete_Code', 'Event_ID', 'Medal_Type', 'Date_Achieved']]

df_final.to_csv('medals_athlete.csv', index=False)

print("Filtered athlete medal data has been saved to 'medals_athlete.csv'.")
