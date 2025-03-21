import mysql.connector

def get_medals_within_date_range(connection, start_date, end_date):
    query = """
    SELECT t.Team_Name, m.Medal_Type, m.Date_Achieved
    FROM Medal m
    JOIN Team t ON m.Team_Code = t.Team_Code
    WHERE m.Date_Achieved BETWEEN %s AND %s
    ORDER BY m.Date_Achieved ASC;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (start_date, end_date))
        results = cursor.fetchall()

        print(f"\nMedals Achieved Between '{start_date}' and '{end_date}':")
        if results:
            for row in results:
                print(f"Team Name: {row[0]}, Medal Type: {row[1]}, Date Achieved: {row[2]}")
        else:
            print("No medals found in the specified date range.")
    
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
    
    finally:
        cursor.close()  # Close the cursor

def main():
    host = 'localhost' 
    user = 'root'  
    password = 'izhary05'  # MySql password
    database = 'WatersportsOlympics_21486144'  

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connection to MySQL database was successful.")

        while True:
            # Display menu
            print("\nMenu:")
            print("1. Find medals achieved within a date range")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                start_date = input("Enter the start date (YYYY-MM-DD): ")
                end_date = input("Enter the end date (YYYY-MM-DD): ")
                get_medals_within_date_range(connection, start_date, end_date)
            elif choice == '2':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select again.")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        if connection.is_connected():
            connection.close()  # Close the database connection
            print("MySQL connection is closed.")

if __name__ == "__main__":
    main()
