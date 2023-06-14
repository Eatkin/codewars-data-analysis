-- https://www.codewars.com/kata/6456759b00c6791f4342bf18
-- 2023-06-02T19:09:16.608+0000
-- Your SQL
SELECT film_id, title, special_features
FROM film
WHERE (('Deleted Scenes' = ANY (special_features) AND 'Behind the Scenes' != ALL (special_features))
   OR ('Behind the Scenes' = ANY (special_features) AND 'Deleted Scenes' != ALL (special_features)))
   AND 'Commentaries' != ALL (special_features)
ORDER BY title, film_id ASC