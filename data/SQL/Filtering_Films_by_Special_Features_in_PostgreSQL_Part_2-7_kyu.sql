-- https://www.codewars.com/kata/64536dc25d1ebb000fa7b9b3
-- 2023-06-02T19:30:44.225+0000
-- Your SQL
SELECT film_id, title, special_features
FROM film
WHERE special_features @> ARRAY['Deleted Scenes', 'Trailers'] AND CARDINALITY(special_features) = 2
ORDER BY title, film_id ASC