CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab;

-- Q1. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- Count will be 0, because we can't compare "NULL"

-- Q2. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- Count will be 2, because we can't compare "NULL" and we have only two values not 5 (6 and 7)

-- Q3. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
-- Count will be 0, because we can't compare "NULL" whic exist in condition

-- Q4. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- Count will be 2, because we can't compare "NULL" and we have only two values not 5 (6 and 7)




