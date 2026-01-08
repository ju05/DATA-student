-- select * from companies
-- select * from employees
-- select * from funtions
-- select * from salaries

-- 🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
CREATE TEMP TABLE df_employee AS
SELECT
	CONCAT(sal.employee_id,'_',CAST(sal.date AS TEXT)) AS id,
	DATE(sal.date) AS month_year,
	*
FROM salaries AS sal
LEFT JOIN employees AS emp
	ON sal.employee_id = emp.employee_code_emp
LEFT JOIN funtions AS fun
	ON sal.func_code = fun.function_code
LEFT JOIN companies AS com
	ON sal.comp_name = com.company_name;
-- DROP TABLE df_employee;

-- 🌟 Exercise 2: Cleaning Data for Consistency and Quality
SELECT * FROM df_employee

UPDATE df_employee
SET
	id = TRIM(id),
	comp_code = TRIM(comp_code),
	comp_name = TRIM(comp_name),
	employee_name = TRIM(employee_name),
	func = TRIM(func),
	comp_code_emp = TRIM(comp_code_emp),
	"GEN" = TRIM("GEN"),
	function = TRIM(function),
	function_group = TRIM(function_group),
	company_name = TRIM(company_name),
	company_city = TRIM(company_city),
	company_state = TRIM(company_state),
	company_type = TRIM(company_type),
	const_site_category = TRIM(const_site_category);

WITH delete_id AS
(
SELECT
	*
FROM df_employee
WHERE id IS NULL
	OR comp_code IS NULL
	OR comp_name IS NULL
	OR employee_name IS NULL
	OR func IS NULL
	OR comp_code_emp IS NULL
	OR "GEN" IS NULL
	OR function IS NULL
	OR function_group IS NULL
	OR company_name IS NULL
	OR company_city IS NULL
	OR company_state IS NULL
	OR company_type IS NULL
	OR const_site_category IS NULL
)

DELETE FROM df_employee
WHERE id IN (SELECT id FROM delete_id);

-- 🌟 Exercise 3 : Calculating Current Employee Counts by Company
SELECT
	comp_name,
	COUNT(*)
FROM df_employee
WHERE 0=0
	AND month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY
	comp_name;

-- 🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time
SELECT
	company_city,
	ROUND((COUNT(*) / SUM(COUNT(*)) OVER()) * 100, 2) AS amount
FROM df_employee
WHERE 0=0
	AND month_year = (SELECT MAX(month_year) FROM df_employee)	
GROUP BY
	company_city;

SELECT
	month_year,
	COUNT(*),
	AVG(COUNT(*)) OVER() AS avg_employee
FROM df_employee
GROUP BY
	month_year;

-- 🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
WITH min_max AS
(
SELECT
	month_year,
	COUNT(*),
	CASE
		WHEN COUNT(*) = MIN(COUNT(*)) OVER() THEN MIN(COUNT(*)) OVER() ELSE 0 END AS MIN,
	CASE
		WHEN COUNT(*) = MAX(COUNT(*)) OVER() THEN MAX(COUNT(*)) OVER() ELSE 0 END AS MAX
FROM df_employee
GROUP BY
	month_year
)
SELECT
	*
FROM min_max
WHERE 0=0
	AND (MIN <> 0 or MAX <> 0);

SELECT
	month_year,
	function_group,
	COUNT(*),
	AVG(COUNT(*)) OVER(PARTITION BY function_group)AS group_avg_employee
FROM df_employee
GROUP BY
	month_year,
	function_group;

SELECT
	EXTRACT(YEAR FROM month_year),
	ROUND(AVG(salary::NUMERIC), 2) AS avg_salary_fun
FROM df_employee
GROUP BY
	EXTRACT(YEAR FROM month_year);