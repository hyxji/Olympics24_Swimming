# Olympics 2024 Water Sports Database Research

## Introduction  
This project aims to organize and manage data related to various water sports events in the Olympics Summer 2024. The database captures essential details about athletes, teams, and disciplines while tracking medals awarded and achievements.  

Key database features include:  
- Foreign keys to maintain relationships between tables and ensure data consistency.  
- Stored procedures to retrieve medal counts based on specific criteria.  
- Triggers to automate updates and ensure data accuracy.  
- Python scripts (using `pandas`) for data population and CRUD operations
- SQL queries for filtering results based on disciplines and date ranges, allowing users to analyze competition performance.  

## Project Structure  
- **`/data`** – Contains datasets from the **Paris 2024 Olympic Summer Games** (*sourced from Kaggle*).  
- **`/src`** – Includes SQL queries and Python scripts for database operations.  
- **`/docs`** – Detailed report covering research, ER diagrams, and project documentation.  

## Key Learning Outcomes  
Throughout this project, I applied various database and programming concepts, including:  
- Subqueries & Constraints – Enforcing data integrity.  
- Stored Procedures & Triggers – Automating key processes.  
- Database Connectivity – Using Python to interact with SQL databases.
- MySQL - Learning MySQL and connecting to Python.

## How to Use  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/olympics-water-sports-db.git
   cd olympics-water-sports-db
2. Import database-schema.sql into your SQL database.
3. Run create_tables.sql to create tables.
4. Source the insert ** .sql files to populate tables.
5. Execute sample queries from /src/queries.sql to analyze data.
6. Create stored procecure file for GetDisciplineDetails.sql or GetAthletesByDiscipline.sql and call the procedures to analyze data.
7. For crud_athletes.py, the script is designed so that you must manually comment out or uncomment the sections you do or do not want to run.
     e.g.  To insert an athlete into the database, uncomment the insert_athlete line and comment out the update_athlete and delete_athlete lines
