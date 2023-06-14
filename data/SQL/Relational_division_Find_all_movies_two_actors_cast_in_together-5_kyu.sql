-- https://www.codewars.com/kata/5817b124e7f4576fd00020a2
-- 2023-05-27T14:19:19.335+0000
SELECT film.title AS title
FROM film
INNER JOIN (
  SELECT film.title, film.film_id
  FROM film
  JOIN
  film_actor
  ON film.film_id = film_actor.film_id
  WHERE film_actor.actor_id = 105
) AS sidney_crowe_films
  ON sidney_crowe_films.film_id = film.film_id
INNER JOIN (
  SELECT film.title, film.film_id
  FROM film
  JOIN
  film_actor
  ON film.film_id = film_actor.film_id
  WHERE film_actor.actor_id = 122
) AS salma_nolte_films
  ON salma_nolte_films.film_id = film.film_id
ORDER BY film.title ASC