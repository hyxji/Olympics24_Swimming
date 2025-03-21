DELIMITER //

CREATE TRIGGER PreventDuplicateEventID
BEFORE INSERT ON Event
FOR EACH ROW
BEGIN
    DECLARE duplicate_count INT;

    -- Check if the Event_ID already exists
    SELECT COUNT(*)
    INTO duplicate_count
    FROM Event
    WHERE Event_ID = NEW.Event_ID;

    -- If it exists, error occurs
    IF duplicate_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Duplicate Event_ID not allowed';
    END IF;
END //

DELIMITER ;
