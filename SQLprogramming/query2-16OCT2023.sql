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
-- Name starts with b and ends with a
SELECT * FROM STUDENT
WHERE first_name LIKE "B%a";
-- Country which starts with U and has two more letters after it
SELECT * FROM STUDENT
WHERE Country LIKE "U__";
-- Names that have 'a' in second place (Combining both wildcards)
SELECT * FROM STUDENT
WHERE first_name LIKE "_a%";

/* IN Operator:
The IN operator is a shorthand for multiple OR conditions. */
SELECT * FROM STUDENT
WHERE date_of_birth in ('2000-03-10', '2001-03-10');

/* The BETWEEN operator is inclusive: begin and end values are included. */
SELECT * FROM STUDENT
WHERE date_of_birth BETWEEN '1998-01-01' AND '2003-12-31';

-- Using ORDERBY to sort the result in ASC AND DESC Order
SELECT * FROM STUDENT
ORDER BY date_of_birth DESC;

SELECT * FROM STUDENT
ORDER BY first_name;

SELECT * FROM STUDENT
ORDER BY Country;

-- First sorts by country and then with firstname where people from same country are not in order! 
-- Checkout o/p of above and below code to understand
SELECT * FROM STUDENT
ORDER BY Country, first_name;

-- check if any column has NULL or not
SELECT * FROM STUDENT
WHERE Country IS NULL;

SELECT * FROM STUDENT
WHERE GENDER IS NOT NULL;





