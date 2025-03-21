import pandas as pd

df_medals = pd.read_csv('medals.csv')
df_events = pd.read_csv('filtered_events_with_event_id.csv')
df_athletes = pd.read_csv('final_filtered_athletes.csv')


df_medals_filtered = df_medals[['medal_type', 'medal_date', 'event', 'code']]

df_merged = pd.merge(df_medals_filtered, df_events[['Event_ID', 'Event_Name']], left_on='event', right_on='Event_Name', how='inner')

df_medals_athlete = df_merged[df_merged['code'].isin(df_athletes['Athlete_Code'])]

df_medals_athlete_final = df_medals_athlete[['code', 'Event_ID', 'medal_type', 'medal_date']].copy()
df_medals_athlete_final = df_medals_athlete_final.rename(columns={
    'code': 'Athlete_Code',
    'medal_type': 'Medal_Type',
    'medal_date': 'Date_Achieved'
})

df_medals_athlete_final.to_csv('medals_athlete.csv', index=False)

print("Filtered athlete medal data has been saved to 'medals_athlete.csv'.")
