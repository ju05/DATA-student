-- 🌟 Exercise 1: DVD Rental

SELECT
	*
FROM language;

SELECT
	film.title,
	film.description,
	lang.name
FROM film as film
LEFT JOIN language as lang
ON film.language_id = lang.language_id;

SELECT
	film.title,
	film.description,
	lang.name
FROM language as lang
LEFT JOIN film as film
ON film.language_id = lang.language_id;

CREATE TABLE new_film(
	id_new_film serial PRIMARY KEY,
	name_new_film VARCHAR (200) NOT NULL
);

INSERT INTO new_film (name_new_film)
VALUES 	('Star Wars'),
		('Hostage'),
		('Clown'),
		('Bad Influence');

DROP TABLE customer_review;

CREATE TABLE customer_review(
	review_id serial PRIMARY KEY,
	film_id INTEGER REFERENCES new_film (id_new_film) ON DELETE CASCADE,
	laguage_id INTEGER REFERENCES language (language_id),
	title VARCHAR (200) NOT NULL,
	score SMALLINT CHECK (score >= 1 AND score <= 10) NOT NULL,
	review_text TEXT NOT NULL,
	last_update DATE NOT NULL
);

INSERT INTO customer_review (film_id, laguage_id, title, score, review_text, last_update)
VALUES 	(2, 2, 'ASDF', 2, 'Not interesting', '20.01.2006'),
		(1, 1, 'Qwerty', 2, 'Very interesting film', '20.01.2006')

DELETE FROM new_film WHERE id_new_film = 2;
-- If I delete film from table new_film it automaticly deletes all related review in customer_review table

-- 🌟 Exercise 2 : DVD Rental

UPDATE film
SET language_id = 4
WHERE film_id = 1;

-- Customer table contain a foreign key from customer.address_id to address.address_id and 
-- it automatically updates customers if the address ID changes
-- you can't delete address that customer still uses

-- You can insert a customer only if the address_id already exists in the address table

-- Yes I can easily drop table customer_review without any consequences

SELECT
	count(*)
FROM rental
WHERE return_date IS NULL;

SELECT
	film.title
FROM rental AS rental
JOIN inventory as inv
	ON 	rental.inventory_id = inv.inventory_id
JOIN film as film
	ON	film.film_id = inv.film_id
WHERE return_date IS NULL
ORDER BY film.replacement_cost DESC
LIMIT 30;


SELECT
	film.title
FROM actor AS actor
JOIN film_actor AS f_actor
	ON	actor.actor_id = f_actor.actor_id
JOIN film AS film
	ON	film.film_id = f_actor.film_id
WHERE	actor.first_name = 'Penelope' 
		AND actor.last_name = 'Monroe'
		AND	film.description ILIKE '%sumo wrestler%'
UNION
SELECT
	film.title
FROM film AS film
JOIN film_category AS f_category
	ON	film.film_id = f_category.film_id
JOIN category AS category
	ON	f_category.category_id = category.category_id
WHERE	film.length < 60
		AND film.rating = 'R'
		AND category.name = 'Documentary'
UNION
SELECT
	film.title
FROM rental AS rental
JOIN customer AS customer
	ON	rental.customer_id = customer.customer_id
JOIN payment AS payment
	ON	rental.rental_id = payment.rental_id
JOIN inventory as inv
	ON 	rental.inventory_id = inv.inventory_id
JOIN film as film
	ON	film.film_id = inv.film_id
WHERE	rental.return_date BETWEEN '28.07.2005' AND '01.08.2005'
		AND customer.first_name = 'Matthew'
		AND customer.last_name = 'Mahan'
		AND payment.amount > 4.00
UNION
SELECT
	*
FROM
(
SELECT
	film.title
FROM rental AS rental
JOIN customer AS customer
	ON	rental.customer_id = customer.customer_id
JOIN inventory as inv
	ON 	rental.inventory_id = inv.inventory_id
JOIN film as film
	ON	film.film_id = inv.film_id
WHERE	customer.first_name = 'Matthew'
		AND customer.last_name = 'Mahan'
		AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
ORDER BY film.replacement_cost DESC
LIMIT 1
);



