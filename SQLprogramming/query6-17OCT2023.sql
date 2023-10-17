USE STUDENTS;
-- Stored procedures (IN/OUT/INOUT)
/* Stored procedures are prepared SQL code that you save so you can reuse it over and over again. 
Here the example would for Age groups to see first_name, last_name, date of joining depending upon the 
age given!
*/
/* IN IN is the default mode. When you define an IN parameter in a stored procedure, 
the calling program has to pass an argument to the stored procedure.
HERE IS EXAMPLE OF IN PARAMETER:
*/
/*In addition, the value of an IN parameter is protected. 
It means that even if you change the value of the IN parameter inside the stored procedure, 
its original value is unchanged after the stored procedure ends. 
In other words, the stored procedure only works on the copy of the IN parameter.
*/
DELIMITER //
CREATE PROCEDURE getStudentsByAge (
IN Agegroup INT
) 
BEGIN
	SELECT first_name, last_name, date_of_joining 
    from STUDENT
    WHERE Age = Agegroup;
END //
DELIMITER ;
 -- Calling the stored Procedure
CALL getStudentsByAge(23);

/* Updating a new column in table Language_to_opt and using 
Stored Procedure depending upon country to fill this column*/
ALTER TABLE student
ADD Language_to_opt VARCHAR(60);

SELECT * FROM STUDENT;
-- CREATING STORED PROCEDURE
DELIMITER //
CREATE PROCEDURE Language_option()
BEGIN 
	UPDATE STUDENT
    SET Language_to_opt = CASE
		WHEN Country = 'China' THEN 'Mandarin'
		WHEN Country = 'South Korea' THEN 'Korean'
		WHEN Country = 'Germany' THEN 'German'
		ELSE 'English'
	END;
END;
//
DELIMITER ;
SET SQL_SAFE_UPDATES = 0;
CALL Language_option();
SELECT * FROM STUDENT;

/* Creating Stored procedure to get count of Students depending on countries */
-- Using OUT 
DELIMITER //
CREATE PROCEDURE GetCountByCountry(
	IN CountryName VARCHAR(50),
	OUT Count INT
)
BEGIN 
	SELECT COUNT(id) 
    INTO Count
    FROM STUDENT
    WHERE Country = CountryName;
END //
DELIMITER ;
CALL GetCountByCountry('UK', @Count);
Select @Count;

/*Using INOUT PARAMETER TO CHECK CHANGES IN THE COUNTER*/
DELIMITER $$
CREATE PROCEDURE SetCounter(
	INOUT counter INT,
    IN inc INT
)
BEGIN
	SET counter = counter + inc;
END$$
DELIMITER ;
SET @counter = 1;
CALL SetCounter(@counter, 1);
SELECT @counter; -- Here the value is 2 in counter
CALL SetCounter(@counter, 3);
SELECT @counter; -- Here the o/p is 5 as it is INOUT it can be altered in the procedure and altered value is returned!
