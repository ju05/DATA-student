-- 🌟 Exercise 1 : Items and customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
SELECT *
FROM items
ORDER BY price ASC;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC;

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT 	first_name,
		last_name
FROM customers
ORDER BY first_name ASC
LIMIT 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT	last_name
FROM customers
ORDER BY last_name DESC;


-- 🌟 Exercise 2 : dvdrental database

SELECT *
FROM customer;

SELECT
	first_name || ' ' || last_name AS full_name
FROM customer;

SELECT 
	DISTINCT(create_date)
FROM customer;

SELECT
	*
FROM customer
ORDER BY first_name DESC;

SELECT
	film_id,
	title,
	description,
	release_year,
	rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT
	*
FROM film
WHERE film_id IN (15, 150);

SELECT
	film_id,
	title,
	description,
	length, 
	rental_rate
FROM film
WHERE title = 'Star wars';

SELECT
	film_id,
	title,
	description,
	length, 
	rental_rate
FROM film
WHERE title ILIKE 'St%';

SELECT
	*
FROM film
ORDER BY replacement_cost ASC
LIMIT 10;

SELECT
	*
FROM 
	(
	SELECT
		*,
		ROW_NUMBER() OVER (ORDER BY replacement_cost ASC) AS row_num
	FROM film
	)
WHERE row_num between 11 AND 20;

SELECT
	c.first_name,
	c.last_name,
	p.amount,
	p.payment_date
FROM customer AS c
LEFT JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

SELECT
	f.*
FROM film AS f
LEFT JOIN inventory AS i
ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

SELECT
	city.city,
	country.country
FROM city AS city
LEFT JOIN country AS country
ON city.country_id = country.country_id;

SELECT
	c.customer_id,
	c.first_name,
	c.last_name,
	p.amount,
	p.payment_date
FROM payment AS p
LEFT JOIN customer AS c
ON p.customer_id = c.customer_id
ORDER BY p.staff_id;
