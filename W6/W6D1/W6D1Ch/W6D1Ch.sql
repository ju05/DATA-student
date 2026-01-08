CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 date_of_birth DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);


insert into actors(first_name, last_name, date_of_birth, number_oscars)
values ('Matt', 'Damon', '06.05.1961', 2);

insert into actors(first_name, last_name, date_of_birth, number_oscars)
values ('Ilia','Demon','08/10/1970', 5);

insert into actors(first_name, last_name, date_of_birth, number_oscars)
values ('Vasya','Octol','08/05/1970', 8);



insert into actors(first_name, last_name, date_of_birth, number_oscars)
values 	('Kostya','Roy','01/05/1970', 1),
		('Boris','Britva','05/06/1970', 6),
		('Vanya','Admund','01/09/1970', 3);



SELECT count(*)
from actors


insert into actors(first_name, last_name, date_of_birth, number_oscars)
values ('Vasya', NULL ,'08/05/1970', 8);

-- We catch the ERROR because we can't insert rows without values.
