-- https://www.codewars.com/kata/5a8f00745084d718940000c5
-- 2023-06-03T16:04:33.825+0000
-- Replace with your SQL Query
SELECT name, weight, price,
ROUND((1000 * price / weight)::numeric, 2)::float AS price_per_kg
FROM Products
ORDER BY price_per_kg, name ASC