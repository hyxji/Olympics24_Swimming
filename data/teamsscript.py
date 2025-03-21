import pandas as pd

df_medals = pd.read_csv('medals.csv')
df_events = pd.read_csv('filtered_events_with_event_id.csv')
df_athletes = pd.read_csv('final_filtered_athletes.csv')  # Contains Athlete_Code
df_teams = pd.read_csv('teams.csv')  # Contains Team_Code as 'code'

print("Medals DataFrame Columns:", df_medals.columns.tolist())
print("Events DataFrame Columns:", df_events.columns.tolist())
print("Athletes DataFrame Columns:", df_athletes.columns.tolist())
print("Teams DataFrame Columns:", df_teams.columns.tolist())

df_medals_filtered = df_medals[df_medals['event'].isin(df_events['Event_Name'])]

df_merged = pd.merge(df_medals_filtered, df_events[['Event_ID', 'Event_Name']], left_on='event', right_on='Event_Name', how='inner')

df_medals_athlete = df_merged[df_merged['code'].isin(df_athletes['Athlete_Code'])]

df_medals_athlete_final = df_medals_athlete[['code', 'Event_ID', 'medal_type', 'medal_date']]
df_medals_athlete_final = df_medals_athlete_final.rename(columns={'code': 'Athlete_Code', 'medal_type': 'Medal_Type', 'medal_date': 'Date_Achieved'})

df_medals_team = df_merged[df_merged['code'].isin(df_teams['code'])]

df_medals_team_final = df_medals_team[['code', 'Event_ID', 'medal_type', 'medal_date']]
df_medals_team_final = df_medals_team_final.rename(columns={'code': 'Team_Code', 'medal_type': 'Medal_Type', 'medal_date': 'Date_Achieved'})

df_medals_athlete_final.to_csv('medals_athlete.csv', index=False)
df_medals_team_final.to_csv('medals_team.csv', index=False)

print("Filtered athlete and team medal data has been saved to 'medals_athlete.csv' and 'medals_team.csv'.")
