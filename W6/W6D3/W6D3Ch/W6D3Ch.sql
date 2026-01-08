-- Part I
CREATE TABLE customer (
	customer_id serial,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(200) NOT NULL,
	PRIMARY KEY (customer_id)
);

CREATE TABLE profile (
	profile_id serial,
	isloggedin BOOLEAN DEFAULT FALSE NOT NULL,
	customer_id INTEGER UNIQUE NOT NULL,
	PRIMARY KEY (customer_id),
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE cascade
);

INSERT INTO
	customer (first_name, last_name)
VALUES
	('John', 'Doe'),
	('Jerome', 'Lalu'),
	('Lea', 'Rive');

INSERT INTO
	profile (isloggedin, customer_id)
VALUES
	(TRUE, (SELECT customer_id FROM customer WHERE first_name='John' LIMIT 1)),
	(DEFAULT, (SELECT customer_id FROM customer WHERE first_name='Jerome' LIMIT 1));
	
SELECT
	customer.first_name
FROM	profile AS profile
JOIN	customer AS customer 
	ON	profile.customer_id = customer.customer_id
WHERE
	profile.isloggedin IS TRUE
	
SELECT
	customer.first_name,
	profile.isloggedin
FROM customer AS customer
LEFT JOIN profile AS profile
	ON	profile.customer_id = customer.customer_id


SELECT
	count(*)
FROM customer AS customer
LEFT JOIN profile AS profile
	ON	profile.customer_id = customer.customer_id
WHERE profile.isloggedin IS NOT TRUE OR profile.isloggedin IS NULL

-- Part II:

CREATE TABLE book (
	book_id SERIAL,
	title VARCHAR(200) NOT NULL,
	author VARCHAR(200) NOT NULL,
	PRIMARY KEY (book_id)
);

INSERT INTO
	book (title, author)
VALUES
	('Alice In Wonderland', 'Lewis Carroll'),
	('Harry Potter', 'J.K Rowling'),
	('To kill a mockingbird', 'Harper Lee');

CREATE TABLE student (
	student_id SERIAL,
	name VARCHAR(200) NOT NULL UNIQUE,
	age SMALLINT CHECK (age >= 1 AND age <= 15) NOT NULL,
	PRIMARY KEY (student_id)
);

INSERT INTO
	student (name, age)
VALUES
	('John', 12),
	('Lera', 11),
	('Patrick', 10),
	('Bob', 14);

CREATE TABLE library (
	book_fk_id INTEGER NOT NULL,
	student_fk_id INTEGER NOT NULL,
	borrowed_date DATE NOT NULL,
	PRIMARY KEY (book_fk_id, student_fk_id),
	FOREIGN KEY (book_fk_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (student_fk_id) REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO
	library (book_fk_id, student_fk_id, borrowed_date)
VALUES
	(
	(SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
	(SELECT student_id FROM student WHERE name = 'John'),
	'15/02/2022'
	),
	(
	(SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
	(SELECT student_id FROM student WHERE name = 'Bob'),
	'03/03/2021'
	),
	(
	(SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
	(SELECT student_id FROM student WHERE name = 'Lera'),
	'23/05/2021'
	),
	(
	(SELECT book_id FROM book WHERE title = 'Harry Potter'),
	(SELECT student_id FROM student WHERE name = 'Bob'),
	'12/08/2021'
	);

SELECT
	*
FROM library;

SELECT
	student.name,
	book.title
FROM library AS library
LEFT JOIN student AS student
	ON	library.student_fk_id = student.student_id
LEFT JOIN book AS book
	ON	library.book_fk_id = book.book_id;

SELECT
	AVG(student.age) AS average_age
FROM library AS library
LEFT JOIN student AS student
	ON	library.student_fk_id = student.student_id
LEFT JOIN book AS book
	ON	library.book_fk_id = book.book_id
WHERE	book.title = 'Alice In Wonderland';

DELETE FROM student WHERE name='Bob';
-- If we delete a student from the student table, he also will be deleted from junction table because of 'ON DELETE CASCADE'



