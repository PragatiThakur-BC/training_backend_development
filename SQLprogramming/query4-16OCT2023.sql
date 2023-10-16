/* Creating two tables Customers and orders to practice handson on Joins*/
USE students;
CREATE TABLE CUSTOMER(
c_id int not null auto_increment,
first_name varchar(30),
primary key(c_id)
);
CREATE TABLE ORDERS(
o_id int not null auto_increment,
amount float,
c_id int,
primary key(o_id),
constraint fk_customerorder foreign key(c_id) references CUSTOMER(c_id)
);
INSERT INTO CUSTOMER(first_name)
VALUES
('John'), ('Robert'),('David'), ('Jen'), ('Betty');
SELECT * FROM CUSTOMER;
ALTER TABLE Orders AUTO_INCREMENT=100;
INSERT INTO ORDERS(amount, c_id)
VALUES
(200, 1), (300, 3), (100, 5), (150, 2), (500, 4), (700, 2);
SELECT * FROM ORDERS;

/* After table creation and data insertion Using joins and understanding what joins are*/

-- INNER JOIN
/*The SQL INNER JOIN command joins two tables based on a 
common column and selects rows with matching values in those columns.*/
SELECT c.c_id, c.first_name, o.amount
from CUSTOMER AS c
INNER JOIN ORDERS AS o
ON c.c_id = o.c_id;
-- INNER JOIN WITH WHERE
SELECT c.c_id, c.first_name, o.amount
from CUSTOMER AS c
INNER JOIN ORDERS AS o
ON c.c_id = o.c_id
WHERE o.amount >150;

-- LEFT JOIN
SELECT c.c_id, c.first_name, o.amount
from CUSTOMER AS c
LEFT JOIN ORDERS AS o
ON c.c_id = o.c_id;

-- Right Join
SELECT c.c_id, c.first_name, o.amount
from CUSTOMER AS c
RIGHT JOIN ORDERS AS o
ON c.c_id = o.c_id;

-- Full outer Join we dont have full outer join here so we will use UNION to get the result on left and right join
/*UNION only returns a unique record, 
while UNION ALL returns all the records (including duplicates).*/
SELECT c.c_id, c.first_name, o.amount
from CUSTOMER AS c
Left JOIN ORDERS AS o
ON c.c_id = o.c_id
UNION
SELECT c.c_id, c.first_name, o.amount
from CUSTOMER AS c
RIGHT JOIN ORDERS AS o
ON c.c_id = o.c_id;

-- GROUP BY CLAUSE
/*
GROUP BY WITH SELECT STATEMENT, 
SEQUENCE: start:- Select < WHERE < groupby < having < orderby -:end
*/
-- Group by on single column
SELECT c_id, SUM(amount) from orders
group by c_id
Having SUM(amount) > 200
ORDER BY SUM(amount);