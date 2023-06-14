-- https://www.codewars.com/kata/5a8ec692b17101bfc70001ba
-- 2023-06-04T16:53:44.417+0000
-- Replace with your SQL Query
SELECT COUNT(id) AS count_products_types, producer
FROM products
GROUP BY producer
ORDER BY count_products_types DESC, producer ASC