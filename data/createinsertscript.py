import pandas as pd

def create_insert_statements(df, table_name):
    insert_statements = []
    for index, row in df.iterrows():
        # Construct the SQL INSERT statement
        sql = f"INSERT INTO {table_name} ("
        sql += ', '.join(row.index) + ") VALUES ("
        sql += ', '.join(f"'{str(x).replace('\'', '\'\'')}'" if pd.notnull(x) else 'NULL' for x in row) + ");"
        insert_statements.append(sql)
    return insert_statements

country_df = pd.read_csv('country.csv')  
country_inserts = create_insert_statements(country_df, 'Country')


discipline_df = pd.read_csv('disciplines.csv')  
discipline_inserts = create_insert_statements(discipline_df, 'Discipline')


venue_df = pd.read_csv('filtered_venues.csv')  
venue_inserts = create_insert_statements(venue_df, 'Venue')


venue_sport_df = pd.read_csv('venue_sport.csv')  
venue_sport_inserts = create_insert_statements(venue_sport_df, 'Venue_Sport')


team_df = pd.read_csv('filtered_teams.csv')  
team_inserts = create_insert_statements(team_df, 'Team')

event_df = pd.read_csv('filtered_events_with_event_id.csv')  
event_inserts = create_insert_statements(event_df, 'Event')

athlete_df = pd.read_csv('final_filtered_athletes.csv')  
athlete_inserts = create_insert_statements(athlete_df, 'Athlete')

medal_df = pd.read_csv('filtered_medals_with_event_id.csv')  
medal_inserts = create_insert_statements(medal_df, 'Medal')


with open('insert_statements.sql', 'w') as f:
    f.write('\n'.join(country_inserts) + '\n')
    f.write('\n'.join(discipline_inserts) + '\n')
    f.write('\n'.join(venue_inserts) + '\n')
    f.write('\n'.join(venue_sport_inserts) + '\n')
    f.write('\n'.join(team_inserts) + '\n')
    f.write('\n'.join(event_inserts) + '\n')
    f.write('\n'.join(athlete_inserts) + '\n')
    f.write('\n'.join(medal_inserts) + '\n')

print("Insert statements written to 'insert_statements.sql'.")
