USE students;
SELECT * FROM STUDENT;

-- using select for differnet conditons and with different keywords
 /* Distinct helps to select unique values */
SELECT DISTINCT Country FROM STUDENT;

/* Using count with distinct to get count of records*/
SELECT COUNT(DISTINCT Country) FROM STUDENT;

-- Using WHERE clause to filter out the data
/* The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE */
SELECT * FROM STUDENT
WHERE Country = "USA";

/* Using where with Numeric Field */
SELECT * FROM STUDENT
WHERE id = 3;

/* Operators in where clause */
/* >, <, =, !=, BETWEEN, >=, <=, IN, LIKE */
SELECT * FROM STUDENT
WHERE id > 2;

SELECT * FROM STUDENT
WHERE id < 5;

SELECT * FROM STUDENT
WHERE id !=4;

SELECT * FROM STUDENT
WHERE id BETWEEN 1 AND 6;

SELECT * FROM STUDENT
WHERE Country in ("USA", "South Korea", "China", "India");

/* There are two wildcards often used in conjunction with the LIKE operator
1. The percent sign % represents zero, one, or multiple characters
2. The underscore sign _ represents one, single character */
-- Name starts with 'a'
SELECT * FROM STUDENT
WHERE first_name LIKE "B%";
-- Name contains 'a'
SELECT * FROM STUDENT
WHERE first_name LIKE "%a%";
-- Last Name ends with 'n'
SELECT * FROM STUDENT
WHERE last_name LIKE "%n";






