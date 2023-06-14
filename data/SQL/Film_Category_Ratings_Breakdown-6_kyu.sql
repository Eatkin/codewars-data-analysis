-- https://www.codewars.com/kata/64354b5b870c66000ff7f4c5
-- 2023-05-21T08:46:57.936+0000
SELECT category.name AS category_name,
rating AS film_rating,
ROUND(100 * COUNT(film.film_id) / SUM(COUNT(film.film_id)) OVER (PARTITION BY category.name), 3) AS percentage
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name, film.rating
ORDER BY category.name ASC, percentage DESC, film.rating ASC