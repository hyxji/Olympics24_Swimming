import pandas as pd

events_df = pd.read_csv('events.csv')  
disciplines_df = pd.read_csv('disciplines.csv')  
venue_sport_df = pd.read_csv('venue_sport.csv')  

disciplines_of_interest = ['Artistic Swimming', 'Marathon Swimming', 'Diving', 'Water Polo', 'Swimming', 'Surfing']
df_filtered = events_df[events_df['sport'].isin(disciplines_of_interest)]

merged_df = df_filtered.merge(disciplines_df, left_on='sport', right_on='Discipline_Name', how='left')

final_df = merged_df.merge(venue_sport_df, left_on='Discipline_Code', right_on='Discipline_Code', how='left')

df_final = final_df[['tag', 'event', 'Discipline_Code', 'Venue_Name']]

df_final.rename(columns={
    'tag': 'Event_Tag',
    'event': 'Event_Name',
    'Venue_Name': 'Venue_Name' 
}, inplace=True)

df_final['Event_ID'] = range(1, len(df_final) + 1)

df_final = df_final[['Event_ID', 'Event_Tag', 'Event_Name', 'Discipline_Code', 'Venue_Name']]

df_final.to_csv('filtered_events_with_event_id.csv', index=False)

print("Filtered event data with Event_ID has been saved to 'filtered_events.csv'.")
