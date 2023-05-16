-- https://www.codewars.com/kata/642ff90503d3e2c9426fd500
-- 2023-05-14T07:09:36.431+0000
SELECT customer.customer_id,
customer.first_name || ' ' || customer.last_name AS full_name,
COUNT(CASE WHEN film.rating != 'NC-17' THEN rental.customer_id END) AS total_rentals
FROM
customer
JOIN rental
ON customer.customer_id = rental.customer_id
JOIN inventory
ON rental.inventory_id = inventory.inventory_id
JOIN film
ON inventory.film_id = film.film_id
GROUP BY customer.customer_id
HAVING COUNT(CASE WHEN film.rating = 'NC-17' THEN rental.customer_id END) = 0
ORDER BY total_rentals DESC, customer.last_name ASC
LIMIT 5