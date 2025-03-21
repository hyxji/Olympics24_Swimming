import pandas as pd
import re

filtered_athletes_df = pd.read_csv('filtered_athletes.csv')
teams_df = pd.read_csv('teams.csv')
disciplines_df = pd.read_csv('disciplines.csv')

# Converts the athletes_codes column to string 
teams_df['athletes_codes'] = teams_df['athletes_codes'].astype(str)

final_athletes_list = []

# Iterate through the filtered athletes
for index, athlete in filtered_athletes_df.iterrows():
    athlete_code = str(athlete['code'])  
    # Matches team code to present athlete
    team_code_matches = teams_df[teams_df['athletes_codes'].str.contains(r'\b' + re.escape(athlete_code) + r'\b', na=False)]
    
    for _, team in team_code_matches.iterrows():
        discipline_name = athlete['disciplines']
        discipline_code_row = disciplines_df[disciplines_df['discipline_name'] == discipline_name]
        discipline_code = discipline_code_row['discipline_code'].values[0] if not discipline_code_row.empty else None
        
        # Append the athlete's details!
        final_athletes_list.append({
            'code': athlete['code'],
            'first_Name': athlete['first_Name'],
            'last_Name': athlete['last_Name'],
            'gender': athlete['gender'],
            'country_code': athlete['country_code'],
            'team_code': team['code'],
            'discipline_code': discipline_code 
        })

# Convert the list of dictionaries to a DataFrame and into a CSV
final_athletes_df = pd.DataFrame(final_athletes_list)
final_athletes_df.to_csv('final_filtered_athletes.csv', index=False)

print("Final athlete data with discipline codes has been saved to 'final_filtered_athletes.csv'.")
