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

