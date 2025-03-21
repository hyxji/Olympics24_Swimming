import mysql.connector

def get_total_medals_for_discipline(connection, discipline_name):
    query = """
    SELECT t.Team_Name, COUNT(m.Medal_Type) AS Total_Medals
    FROM Medal m
    JOIN Team t ON m.Team_Code = t.Team_Code
    JOIN Discipline d ON t.Discipline_Code = d.Discipline_Code
    WHERE d.Discipline_Name = %s
    GROUP BY t.Team_Name
    ORDER BY Total_Medals DESC;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (discipline_name,))
        results = cursor.fetchall()

        # Print the results
        print(f"\nTotal Medals for Each Team in '{discipline_name}':")
        if results:
            for row in results:
                print(f"Team Name: {row[0]}, Total Medals: {row[1]}")
        else:
            print(f"No medals found for the discipline: '{discipline_name}'.")
    
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
            print("1. Find total medals for a discipline")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                discipline_name = input("Enter the name of the discipline: ")
                get_total_medals_for_discipline(connection, discipline_name)
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
