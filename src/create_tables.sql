-- Create Country table
CREATE TABLE Country (
    Country_Code CHAR(3) PRIMARY KEY,
    Country_Name VARCHAR(100) NOT NULL
);

-- Create Discipline table
CREATE TABLE Discipline (
    Discipline_Code VARCHAR(50) PRIMARY KEY,
    Discipline_Name VARCHAR(50) NOT NULL
);

-- Create Venue table
CREATE TABLE Venue (
    Venue VARCHAR(100) PRIMARY KEY,
    Date_Start DATETIME NOT NULL,
    Date_End DATETIME NOT NULL
);

-- Create Event table (now with Event_ID as the primary key)
CREATE TABLE Event (
    Event_ID VARCHAR(50) PRIMARY KEY, 
    Event_Tag VARCHAR(50) NOT NULL,     
    Event_Name VARCHAR(100) NOT NULL,
    Discipline_Code VARCHAR(50) NOT NULL,
    Venue VARCHAR(100) NOT NULL,
    FOREIGN KEY (Discipline_Code) REFERENCES Discipline(Discipline_Code) ON DELETE CASCADE,
    FOREIGN KEY (Venue) REFERENCES Venue(Venue) ON DELETE CASCADE
);


CREATE TABLE Team (
    Team_Code VARCHAR(50) PRIMARY KEY,
    Team_Name VARCHAR(50) NOT NULL,
    Team_Gender CHAR(1) NOT NULL CHECK (Team_Gender IN ('M', 'F', 'X','O')),
    Country_Code CHAR(3) NOT NULL,
    Discipline_Code VARCHAR(50) NOT NULL,
    Event_Tag VARCHAR(50), 
    FOREIGN KEY (Country_Code) REFERENCES Country(Country_Code) ON DELETE CASCADE,
    FOREIGN KEY (Discipline_Code) REFERENCES Discipline(Discipline_Code) ON DELETE CASCADE
);

-- Create Athlete table (Team reference can be null)
CREATE TABLE Athlete (
    Athlete_Code VARCHAR(50) PRIMARY KEY,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Gender VARCHAR(50) NOT NULL,
    Country_Code CHAR(3) NOT NULL,
    Team_Code VARCHAR(50) NULL,
    Discipline_Code VARCHAR(50) NOT NULL,
    FOREIGN KEY (Country_Code) REFERENCES Country(Country_Code) ON DELETE CASCADE,
    FOREIGN KEY (Team_Code) REFERENCES Team(Team_Code) ON DELETE SET NULL,
    FOREIGN KEY (Discipline_Code) REFERENCES Discipline(Discipline_Code) ON DELETE CASCADE
);

-- Create Medal table
CREATE TABLE Medal (
    Team_Code VARCHAR(50) NOT NULL,
    Event_ID VARCHAR(50),  
    Medal_Type VARCHAR(20) NOT NULL CHECK (Medal_Type IN ('Gold Medal', 'Silver Medal', 'Bronze Medal')),
    Date_Achieved DATE NOT NULL,
    PRIMARY KEY (Team_Code, Event_ID),
    FOREIGN KEY (Team_Code) REFERENCES Team(Team_Code) ON DELETE CASCADE,
    FOREIGN KEY (Event_ID) REFERENCES Event(Event_ID) ON DELETE CASCADE
);

-- Create Venue_Sport table
CREATE TABLE Venue_Sport (
    Venue VARCHAR(100),
    Discipline_Code VARCHAR(50),
    PRIMARY KEY (Venue, Discipline_Code),
    FOREIGN KEY (Venue) REFERENCES Venue(Venue) ON DELETE CASCADE,
    FOREIGN KEY (Discipline_Code) REFERENCES Discipline(Discipline_Code) ON DELETE CASCADE
);
