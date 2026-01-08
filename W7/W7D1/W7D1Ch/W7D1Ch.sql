-- Create the employees table
CREATE TABLE employes (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

-- Insert 20 sample records 
INSERT INTO employes (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

-- Identify and handle any missing value.
WITH empty_row AS
(
SELECT
	employee_id
FROM employes
WHERE
	employee_id IS NULL
	OR employee_name IS NULL
	OR salary IS NULL
	OR hire_date IS NULL
	OR department IS NULL
)
DELETE FROM employes
WHERE employee_id IN (SELECT employee_id FROM empty_row);

-- Check for and eliminate any duplicate rows in the dataset.
SELECT
	*
FROM 
	(
	SELECT
		*,
		ROW_NUMBER() OVER(PARTITION BY employee_id, employee_name, salary, hire_date, department) AS dubl
	FROM employes
	)
WHERE 0=0
	AND dubl <>  1;

-- Correct any structural issues, such as inconsistent naming conventions or formatting errors.
-- Ensure all columns have appropriate data types (e.g. the hire_date column).
ALTER TABLE employes
ALTER COLUMN hire_date TYPE DATE
USING hire_date::DATE;



WITH salary_stats AS (
  SELECT 
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3
  FROM employes
),
iqr_bounds AS (
  SELECT 
    q1,
    q3,
    (q3 - q1) AS iqr,
    q1 - 1.5 * (q3 - q1) AS lower_bound,
    q3 + 1.5 * (q3 - q1) AS upper_bound
  FROM salary_stats
)
SELECT 
  e.*,
  s.lower_bound,
  s.upper_bound,
  CASE
    WHEN e.salary < s.lower_bound OR e.salary > s.upper_bound THEN 'OUTLIER'
    ELSE 'NORMAL'
  END AS outlier_status
FROM employes e
CROSS JOIN iqr_bounds s;

-- Standardize and normalize data where applicable to ensure consistency.
UPDATE employes
SET employee_name = INITCAP(LOWER(employee_name));

UPDATE employes
SET department = 'Unknown'
WHERE department IS NULL;

UPDATE employes
SET department = INITCAP(TRIM(department));

WITH salary_bounds AS (
  SELECT 
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
  FROM employes
)
SELECT 
  employee_id,
  employee_name,
  salary,
  ROUND((salary - sb.min_salary) / NULLIF(sb.max_salary - sb.min_salary, 0), 4) AS salary_normalized
FROM employes e
CROSS JOIN salary_bounds sb;





