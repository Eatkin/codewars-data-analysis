-- https://www.codewars.com/kata/645362d917686c000f88a8fe
-- 2023-06-02T19:27:27.410+0000
-- Your SQL
SELECT film_id, title, special_features
FROM film
WHERE ('Trailers' = ANY (special_features) AND 'Deleted Scenes' = ANY (special_features))
ORDER BY title, film_id ASC