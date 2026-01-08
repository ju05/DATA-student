CREATE TABLE items(
 items_id SERIAL PRIMARY KEY,
 item VARCHAR (100) NOT NULL,
 price INTEGER NOT NULL
);

CREATE TABLE customers(
 customers_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL
);

insert into items (item, price)
values 	('Small Desk', 100),
		('Large desk', 300),
		('Fan', 80);

insert into customers (first_name, last_name)
values 	('Greg', 'Jones'),
		('Sandra', 'Jones'),
		('Scott', 'Scott'),
		('Trevor', 'Green'),
		('Melanie', 'Johnson');


-- All the items.
select *
from items;

-- All the items with a price above 80 (80 not included).
select *
from items
where price > 80;

-- All the items with a price below 300. (300 included)
select *
from items
where price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
select *
from customers
where last_name = 'Smith';

-- All customers whose last name is ‘Jones’.
select *
from customers
where last_name = 'Jones';

-- All customers whose firstname is not ‘Scott’.
select *
from customers
where first_name <> 'Scott';

