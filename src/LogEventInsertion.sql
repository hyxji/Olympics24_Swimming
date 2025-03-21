DELIMITER //

CREATE TRIGGER LogEventInsertion
AFTER INSERT ON Event
FOR EACH ROW
BEGIN
    INSERT INTO Event_Log (Event_ID, Event_Name)
    VALUES (NEW.Event_ID, NEW.Event_Name);
END //

DELIMITER ;
