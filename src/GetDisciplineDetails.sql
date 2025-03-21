DELIMITER //

CREATE PROCEDURE GetDisciplineDetails(IN p_Discipline_Code VARCHAR(50))
BEGIN
    SELECT 
        d.Discipline_Name, 
        COUNT(a.Athlete_Code) AS Athlete_Count
    FROM 
        Discipline d
    LEFT JOIN 
        Athlete a ON d.Discipline_Code = a.Discipline_Code
    WHERE 
        d.Discipline_Code = p_Discipline_Code
    GROUP BY 
        d.Discipline_Name;
END //

DELIMITER ;
