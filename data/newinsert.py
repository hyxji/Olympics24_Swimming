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

medal_df = pd.read_csv('medals_team.csv')
medal_inserts = create_insert_statements(medal_df, 'Medal')

def write_to_file(insert_statements, file_name):
    with open(file_name, 'w') as f:
        f.write('\n'.join(insert_statements) + '\n')

write_to_file(country_inserts, 'insert_country.sql')
write_to_file(discipline_inserts, 'insert_discipline.sql')
write_to_file(venue_inserts, 'insert_venue.sql')
write_to_file(venue_sport_inserts, 'insert_venue_sport.sql')
write_to_file(team_inserts, 'insert_team.sql')
write_to_file(event_inserts, 'insert_event.sql')
write_to_file(athlete_inserts, 'insert_athlete.sql')
write_to_file(medal_inserts, 'insert_medal.sql')

print("Insert statements written to separate SQL files.")
