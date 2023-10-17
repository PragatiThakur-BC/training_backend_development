-- CREATE DATABASE students;
USE students;
drop table student;
-- Create table student
CREATE TABLE STUDENT(
id INT NOT NULL auto_increment,
first_name varchar(30),
last_name varchar(30),
date_of_birth date,
date_of_joining date,
gender char,
primary key(id)
);

-- Lists all the tables in a particular database
SELECT table_name
FROM information_schema.tables
WHERE table_type='BASE TABLE'
      AND table_schema = 'students';

-- Describing table structure
SHOW COLUMNS FROM STUDENT;
-- Inserting data to student table
INSERT INTO STUDENT(
	first_name,
    last_name,
    date_of_birth,
    date_of_joining,
    gender
)
VALUES
(
	'Bella',
    'Valentine',
    '2000-03-10',
    current_date(),
    'F'
),
(
	'Mark',
    'Wood',
    '2001-03-10',
    current_date(),
    'M'
),
(
	'David',
    'Jhonson',
    '1999-02-10',
    current_date(),
    'M'
);
-- viewing all the data of database
SELECT * FROM STUDENT;
-- Altering table to add country column
ALTER TABLE student
ADD Country varchar(50);
-- Updating values to Country column
UPDATE student
SET Country = 'USA'
WHERE id in (1, 2, 3);
-- Adding few more records to database
INSERT INTO STUDENT(
	first_name,
    last_name,
    date_of_birth,
    date_of_joining,
    gender,
    Country
)
VALUES
(
	'Ricky',
    'Dwell',
    '1998-04-20',
    current_date(),
    'M',
    'UK'
),
(
	'Hao',
    'Ren',
    '2000-07-13',
    current_date(),
    'M',
    'China'
),
(
	'Ji Woong',
    'kim',
    '1997-10-08',
    current_date(),
    'M',
    'South Korea'
);
-- Lets Look at the table
SELECT * FROM student;

-- inserting data for computations which were done on 17 OCT file
INSERT INTO STUDENT(
	first_name,
    last_name,
    date_of_birth,
    date_of_joining,
    gender,
    Country,
    Age
)
VALUES
(
	'William',
    'William',
    '1999-06-20',
    current_date(),
    'M',
    'UK',
    23
);





