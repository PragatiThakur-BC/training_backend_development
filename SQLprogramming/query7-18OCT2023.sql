USE STUDENTS;
SHOW TABLES;
-- Creating Triggers
-- Before Insert Trigger to verify the age
DELIMITER //
CREATE TRIGGER age_verify
BEFORE INSERT ON STUDENT
FOR EACH ROW
IF NEW.Age <= 20 THEN SET NEW.Age = 20; -- As the min age for this grade students can be 20!
end if; //
INSERT INTO STUDENT(
	first_name,
    last_name,
    date_of_birth,
    date_of_joining,
    gender,
    Country,
    Age,
    Language_to_opt
)
VALUE('Jackson', 'Wang', '1997-09-25', current_date(),'M', 'China', 10, 'Mandarin'); -- Here we are giving age as 10
SELECT * FROM STUDENT
WHERE id = 14 ;

-- 	AFTER INSERT TRIGGER
/*Creating Another Table to store messages when we will use trigger on student table after insertion of record*/
CREATE TABLE MESSAGE(
	id int auto_increment,
    message varchar(350) not null,
    PRIMARY KEY(id)
);
-- CREATING TRIGGER check language_check_null for opting this language in Student database
DELIMITER //
CREATE TRIGGER language_check_null
AFTER INSERT ON STUDENT
FOR EACH ROW
BEGIN
	IF NEW.Language_to_opt is NULL THEN 
	INSERT INTO MESSAGE(message)
	VALUES(concat('Hi', new.first_name, ', Please opt atleast one Language'));
	END IF;
END //
DELIMITER ;

INSERT INTO STUDENT(
	first_name,
    last_name,
    date_of_birth,
    date_of_joining,
    gender,
    Country,
    Age,
    Language_to_opt
)
VALUES
(
	'Henry',
    'Williams',
    '1997-03-22',
    current_date(),
    'M',
    'UK',
    7,
    NULL
),
(	
	'Richard',
    'John',
    '1998-03-22',
    current_date(),
    'M',
    'USA',
    25,
    NULL
);
SELECT * FROM STUDENT;
SELECT * FROM MESSAGE;

-- Trigger before UPDATE
/* We will fill the Language_to_opt column if it is null depending on the Country*/
DELIMITER //
CREATE TRIGGER fill_Language_option
BEFORE UPDATE ON STUDENT
FOR EACH ROW
BEGIN
 SET NEW.Language_to_opt = CASE
		WHEN NEW.Country = 'China' THEN 'Mandarin'
		WHEN NEW.Country = 'South Korea' THEN 'Korean'
		WHEN NEW.Country = 'Germany' THEN 'German'
		ELSE 'English'
	END;
END //
DELIMITER ;

SET SQL_SAFE_UPDATES = 0;
UPDATE STUDENT
SET Language_to_opt = '';
SELECT * FROM STUDENT;
UPDATE STUDENT 
SET Age = 24
WHERE id = 13;
