-- https://www.codewars.com/kata/5a8ed96bfd8c066e7f00011a
-- 2023-06-04T16:51:01.701+0000
-- Replace with your SQL Query
SELECT COUNT(id) AS products, country
FROM products
WHERE country IN ('United States of America', 'Canada')
GROUP BY country
ORDER BY products DESC