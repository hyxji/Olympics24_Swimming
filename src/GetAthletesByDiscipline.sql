DELIMITER //

CREATE PROCEDURE GetAthletesByDiscipline(
    IN discipline VARCHAR(50)
)
BEGIN
    SELECT Athlete_Code, First_Name, Last_Name, Gender, Country_Code, Team_Code
    FROM Athlete
    WHERE Discipline_Code = discipline;
END //

DELIMITER ;
