-- https://www.codewars.com/kata/5a8eb3fb57c562110f0000a1
-- 2023-06-04T16:55:40.484+0000
-- select all of the items
SELECT id, name, stock
FROM products
WHERE stock <= 2 AND producent = 'CompanyA'
ORDER BY id ASC