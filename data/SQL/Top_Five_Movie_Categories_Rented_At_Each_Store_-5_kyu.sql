-- https://www.codewars.com/kata/642d3e2c6555a30d83798f54
-- 2023-06-12T11:41:26.243+0000
SELECT store_id, category, num_rentals
FROM (
  SELECT
    inventory.store_id AS store_id,
    category.name AS category, 
    COUNT(film_category.category_id) AS num_rentals,
    ROW_NUMBER() OVER (PARTITION BY inventory.store_id ORDER BY COUNT(film_category.category_id) DESC, category.name ASC) AS rn
  FROM rental
    JOIN inventory
    ON rental.inventory_id = inventory.inventory_id
    JOIN film_category
    ON inventory.film_id = film_category.film_id
    JOIN category
    ON film_category.category_id = category.category_id
  GROUP BY inventory.store_id, category.name
  ) AS subquery
WHERE rn <= 5
ORDER BY store_id, num_rentals DESC, category