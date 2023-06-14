-- https://www.codewars.com/kata/644258f853c27ca88cfc29b0
-- 2023-06-02T16:07:28.071+0000
-- The plan:
-- Join customers with rental on customer.customer_id = rental.customer_id where rental date is in May, June and July of 2005
-- Join rental table with inventory on rental.inventory_id = inventory.inventory_id
-- Join inventory table with film_category on inventory.film_id = film_category.film_id
-- Join film_category to category on film_category.category_id = category.category_id
-- Group by the category and return category.name as genre and count(category.name) as total_rentals
-- Order by total_rentals DESC and then genre ASC
SELECT category.name AS genre, COUNT(category.name) AS total_rentals
FROM  (
  SELECT customer.customer_id
  FROM customer
  INNER JOIN rental
  ON customer.customer_id = rental.customer_id
  WHERE DATE_PART('year', rental.rental_date) = 2005
  AND DATE_PART('month', rental.rental_date) IN (5, 6, 7)
  GROUP BY customer.customer_id
  HAVING COUNT(DISTINCT DATE_PART('month', rental.rental_date)) = 3
) AS customers_restricted
JOIN rental
ON customers_restricted.customer_id = rental.customer_id
JOIN inventory
ON rental.inventory_id = inventory.inventory_id
JOIN film_category
ON inventory.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
GROUP BY category.name
ORDER BY total_rentals DESC, genre ASC
LIMIT 5