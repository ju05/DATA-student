-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. 
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.
with rate_budget as
(
select
	comp.company_name,
	movie.release_date,
	movie.title,
	movie.budget,
	movie.budget - lag(movie.budget, 1) over(partition by comp.company_id order by movie.release_date) as gr_rate
from movies.movie as movie
left join movies.movie_company as mov_comp
	on	movie.movie_id = mov_comp.movie_id
left join movies.production_company as comp
	on	mov_comp.company_id = comp.company_id
)
select
	company_name,
	avg(gr_rate)
from rate_budget
group by
	company_name

-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. 
-- Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

with movie_vote as
(
select
	movie_id,
	vote_average,
	avg(vote_average) over() as avg_vote
from movies.movie as movie
)
select
	person.person_id,
	person.person_name
from movie_vote as movie
left join movies.movie_cast as actor
	on movie.movie_id = actor.movie_id
left join movies.person as person
	on actor.person_id = person.person_id
where 0=0
	and vote_average > avg_vote
group by
	person.person_id
order by
	count(*) desc
limit 1

-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, 
-- considering only the last three movies released in the genre. 
-- Use window functions with the ROWS frame specification to achieve this.

select
	movie.title,
	genre.genre_name,
	movie.revenue,
	movie.release_date,
	avg(revenue) over(partition by genre.genre_id order by movie.release_date ROWS 3 PRECEDING) as rollling_avg
from movies.movie as movie
left join movies.movie_genres as mov_gen
	on	movie.movie_id = mov_gen.movie_id
left join movies.genre as genre
	on	mov_gen.genre_id = genre.genre_id
	
-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. 
-- Use window functions and CTEs to group movies by their series and calculate the total revenue.

with words_revenue as
(
select
	keyword.keyword_name,
	sum(movie.revenue),
	row_number() over(order by sum(movie.revenue) desc) as reting
from movies.movie as movie
left join movies.movie_keywords as mov_key
	on movie.movie_id = mov_key.movie_id
left join movies.keyword as keyword
	on	keyword.keyword_id = mov_key.keyword_id
group by
	keyword.keyword_name
)
select
	*
from words_revenue
where 0=0
	and reting = 1