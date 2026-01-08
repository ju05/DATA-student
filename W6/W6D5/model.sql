// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table movies.country {
  country_id integer [primary key]
  country_iso_code integer
  country_name integer
}

Table movies.genre {
  genre_id integer [primary key]
  genre_name integer
}

Table movies.department {
  department_id integer [primary key]
  department_name integer
}

Table movies.gender {
  gender_id integer [primary key]
  gender integer
}

Table movies.keyword {
  keyword_id integer [primary key]
  keyword_name integer
}

Table movies.language {
  language_id integer [primary key]
  language_name integer
  language_code integer
}

Table movies.language_role {
  role_id integer [primary key]
  language_role integer
}

Table movies.movie {
  movie_id integer [primary key]
  title integer
  budget integer
  homepage integer
  overview integer
  popularity integer
  release_date integer
  revenue integer
  runtime integer
  movie_status integer
  tagline integer
  vote_average integer
  vote_count integer
}

Table movies.movie_genre {
  movie_id integer
  genre_id integer
}

Table movies.movie_company {
  movie_id integer
  company_id integer
}

Table movies.production_company {
  company_id integer [primary key]
  company_name integer
}










Ref: "movies"."movie"."movie_id" < "movies"."movie_genre"."movie_id"

Ref: "movies"."movie_genre"."genre_id" < "movies"."genre"."genre_id"

Ref: "movies"."movie"."movie_id" < "movies"."movie_company"."movie_id"

Ref: "movies"."movie_company"."company_id" < "movies"."production_company"."company_id"