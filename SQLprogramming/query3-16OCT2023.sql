USE students;
/* LIMIT OR TOP OR FETCH FIRST OR ROWNUM Clause Do the same things but for differnt databases
here in MySQL Workbench we use limit */
-- limit : clause is used to specify the number of records to return.
SELECT * FROM STUDENT
WHERE Country = "uk"
LIMIT 1;

-- First 4 records of STUDENT TABLE
SELECT * FROM STUDENT
LIMIT 4;

/* Adding age column to table */
ALTER TABLE STUDENT
ADD COLUMN Age INT;

SET SQL_SAFE_UPDATES = 0;
UPDATE STUDENT
SET AGE = timestampdiff(YEAR, date_of_birth, CURDATE());
SELECT * FROM STUDENT;

/* MIN AND MAX FUNCTIONS */
-- we are going to apply on age column 
SELECT MIN(Age) as Youngest_Person
FROM STUDENT;

SELECT MAX(Age) as Oldest_Person
FROM STUDENT;

/* Using COUNT() Function to get count of record based on condition given */
SELECT COUNT(*) FROM STUDENT
WHERE Age > 23;

/* to get unique and remove duplicates we will use DISTINCT  */
SELECT count(DISTINCT Age) FROM STUDENT; 
/* USING ALIAS */
SELECT count(distinct Age) as Unique_Age FROM Student;

/* USING SUM() FUNCTION ON AGE (Even though here we cant do much with this) 
but we can use this funct with expressions also like SUM(Price * Quantity) */
SELECT SUM(Age) AS Sum_of_Age FROM STUDENT;

/* Finding the AVG() Age WE CAN APPLY WHERE CONDIDITONS ALSO TO any of the functions we have used */
SELECT AVG(Age) AS Average_Age_Of_Students FROM STUDENT;

/* CONCAT() TO GET FULL_NAME OF STUDENTS*/
SELECT CONCAT(first_name,' ',last_name) as Full_Name
FROM STUDENT;
