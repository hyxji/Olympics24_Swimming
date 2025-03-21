import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',      
            user='root',   
            password='izhary05',# MySQL password
            database='WatersportsOlympics_21486144' 
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful.")
            return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

#Insert an athlete
def insert_athlete(connection, athlete_code, first_name, last_name, gender, country_code, team_code, discipline_code):
    query = """
    INSERT INTO Athlete (Athlete_Code, First_Name, Last_Name, Gender, Country_Code, Team_Code, Discipline_Code)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    data = (athlete_code, first_name, last_name, gender, country_code, team_code, discipline_code)
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)   # Execute the insert query
        connection.commit()            # Commit the transaction
        print("Athlete inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error inserting athlete: {e}")
    finally:
        cursor.close()                # Close the cursor

# Update an athlete
def update_athlete(connection, athlete_code, new_team_code):
    query = """
    UPDATE Athlete
    SET Team_Code = %s
    WHERE Athlete_Code = %s;
    """
    data = (new_team_code, athlete_code)
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)   # Execute the update query
        connection.commit()            # Commit the transaction
        print("Athlete updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating athlete: {e}")
    finally:
        cursor.close()                # Close the cursor

#Delete an athlete
def delete_athlete(connection, athlete_code):
    query = """
    DELETE FROM Athlete
    WHERE Athlete_Code = %s;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (athlete_code,))  # Execute the delete query
        connection.commit()            # Commit the transaction
        print("Athlete deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting athlete: {e}")
    finally:
        cursor.close()                # Close the cursor

#Close the connection
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

#Main function
def main():
    connection = create_connection() 
    if connection:
        # Insert an athlete 
        #insert_athlete(connection, '9999999', 'John', 'Doe', 'Male', 'USA', 'SWAWTEAM8---USA01', 'artistic-swimming')
        
        # Update the athlete's team
        #update_athlete(connection, '9999999', 'DIVM10MTEAM2UKR01')

        # Delete the athlete 
        delete_athlete(connection, '9999999')

        close_connection(connection) # Close the connection

if __name__ == "__main__":
    main()
