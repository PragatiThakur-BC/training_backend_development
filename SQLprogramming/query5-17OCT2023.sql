USE STUDENTS;
SELECT * FROM STUDENT;
-- LETS ADD FEW MORE ENTRIES:
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
	'Bella',
    'Rich',
    '1999-07-25',
    current_date(),
    'F',
    'Germany'
),
(
	'Isla',
    'Walsh',
    '2001-11-13',
    current_date(),
    'F',
    'Germany'
),
(
	'Oscar',
    'Brown',
    '1998-01-08',
    current_date(),
    'M',
    'USA'
);
SELECT * FROM STUDENT;
UPDATE STUDENT
SET Age = 24
WHERE id Between 7 AND 9;

-- SQL CASE EXPRESSION
/* The CASE expression goes through conditions and returns a value when the first condition is met 
(like an if-then-else statement). So, once a condition is true, it will stop reading and return the result. 
If no conditions are true, it returns the value in the ELSE clause.
*/

SELECT first_name, last_name, Age,
CASE
	WHEN Age = 24 THEN 'Age is 24'
    WHEN Age > 24 THEN 'Age is Greater than 24'
    ELSE 'Age less than 24'
END AS Age_Criteria
FROM STUDENT;

-- SQL NULL FUNCTIONS 
/* Lets insert few data records which has Null values so that we cam look into
different Null functions in sql */
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
	'Jennifer',
    'Margeret',
    '2001-07-30',
    current_date(),
    'F',
    'Australia'
),
(
	'Jacob',
    'Walsh',
    '2001-09-23',
    current_date(),
    'M',
    'UK'
);
SELECT * FROM STUDENT;
-- ISNULL()
/* Lets look at students name who have null value in age and later count of them*/
SELECT first_name, last_name 
FROM STUDENT
WHERE isnull(Age);

SELECT COUNT(*) AS Count_of_Null_value_of_age
FROM STUDENT
WHERE isnull(Age);

-- COALESCE() Function
/* The SQL COALESCE() function returns the first occurred NON-NULL expression among its arguments. 
If all the expressions are NULL, then the COALESCE() function will return NULL.
*/
SELECT coalesce(NULL, 'Work', 'Office');
-- Applying on student table on dob and age
SELECT first_name, last_name, coalesce(Age, date_of_birth) AS Result
FROM Student;

-- NULLIF() Function
/*The SQL NULLIF() function compares two expressions. If both expressions are the same, it returns NULL. 
Otherwise, it returns the first expression. 
This function can be used directly with clauses like SELECT, WHERE, and GROUP BY.*/
SELECT first_name, last_name, nullif(first_name, last_name) AS NULLIF_RESULT
FROM STUDENT;

-- Checks if first_name and last_name are same if yes gives first_name & last_name of the record
SELECT first_name, last_name
FROM STUDENT
WHERE NULLIF(first_name, last_name) IS NULL;