-- CREATE DATABASE students;
USE students;
drop table student;
-- Create table student
CREATE TABLE STUDENT(
id INT NOT NULL,
first_name varchar(30),
last_name varchar(30),
date_of_birth date,
date_of_joining date,
gender char
);

-- Lists all the tables in a particular database
SELECT table_name
FROM information_schema.tables
WHERE table_type='BASE TABLE'
      AND table_schema = 'students'
