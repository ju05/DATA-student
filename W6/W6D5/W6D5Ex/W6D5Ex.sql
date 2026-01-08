-- Task 1: Rank Movies by Popularity within Each Genre

-- Use the RANK() function to rank movies by their popularity within each genre. 
-- Display the genre name, movie title, and their rank based on popularity.


select 
	movie.title,
	genre.genre_name,
	rank() over(partition by genre.genre_name order by movie.popularity desc)
from movies.movie as movie
left join movies.movie_genres as mov_gen
	on	movie.movie_id = mov_gen.movie_id
left join movies.genre as genre
	on	mov_gen.genre_id = genre.genre_id


-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

-- Use the NTILE() function to divide the movies produced by each production 
-- company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.

select
	prod_comp.company_name,
	movie.title,
	movie.revenue,
	NTILE(4) over (partition by prod_comp.company_id order by movie.revenue)
from movies.movie as movie
left join movies.movie_company as mov_com
	on	movie.movie_id = mov_com.movie_id
left join movies.production_company as prod_comp
	on	mov_com.company_id = prod_comp.company_id

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate 
-- the running total of movie budgets within each genre.
-- Display the genre name, movie title, budget, and running total budget.

select 
	movie.title,
	genre.genre_name,
	movie.budget,
	sum(movie.budget) over (partition by genre.genre_name order by movie.budget)
from movies.movie as movie
left join movies.movie_genres as mov_gen
	on	movie.movie_id = mov_gen.movie_id
left join movies.genre as genre
	on	mov_gen.genre_id = genre.genre_id

-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie
-- within each genre based on the release date.
-- Display the genre name, movie title, and release date.

with last_film as
(
select 
	movie.title,
	genre.genre_name,
	movie.release_date,
	FIRST_VALUE(movie.title) over (partition by genre.genre_name order by movie.release_date DESC) as recent_movie
from movies.movie as movie
left join movies.movie_genres as mov_gen
	on	movie.movie_id = mov_gen.movie_id
left join movies.genre as genre
	on	mov_gen.genre_id = genre.genre_id
)

select
	max(release_date),
	genre_name,
	recent_movie as title
from last_film
group by 
	recent_movie,
	genre_name;


-- 🌟 Exercise 2: Cast and Crew Performance Analysis

-- Task 1: Rank Actors by Their Appearance in Movies

-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. 
-- Display the actor’s name and their rank.

select 
	person.person_id,
	count(*) as movie_count,
	dense_rank() over (order by count(*) DESC) as rank
from movies.movie as movie
left join movies.movie_cast as mov_cast
	on	movie.movie_id = mov_cast.movie_id
left join movies.person as person
	on	mov_cast.person_id = person.person_id
group by 
	person.person_id

-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with he highest average movie rating. 
-- Display the director’s name and their average rating.

with new_table as
(
select
	person.person_name,
	avg(vote_average) as avg_rating,
	rank() over (order by avg(vote_average) desc) as rank_director
from movies.movie as movie
left join movies.movie_crew as mov_crew
	on	movie.movie_id = mov_crew.movie_id
left join movies.person as person
	on	mov_crew.person_id = person.person_id
where 0=0
	and mov_crew.job = 'Director'
group by
	person.person_id
)
select
	*
from new_table

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor.
-- Display the actor’s name and the cumulative revenue.

select
	person.person_name,
	sum(movie.revenue) over(partition by person.person_id order by movie.movie_id)
from movies.movie_cast as mov_cast
left join movies.movie as movie
	on	movie.movie_id = mov_cast.movie_id
left join movies.person as person
	on	mov_cast.person_id = person.person_id

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have the highest total budget.
-- Display the director’s name and the total budget.

with person_by_budget as
(
select
	person.person_name,
	sum(movie.budget) as total_budget,
	row_number() over(order by sum(movie.budget) DESC) as hiest_budget
from movies.movie as movie
left join movies.movie_crew as mov_crew
	on	movie.movie_id = mov_crew.movie_id
left join movies.person as person
	on	mov_crew.person_id = person.person_id
where 0=0
	and mov_crew.job = 'Director'
group by
	person.person_id
)
select
	*
from person_by_budget
where 0=0
	and hiest_budget = 1

