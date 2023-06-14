-- https://www.codewars.com/kata/57a0885cbb9944e24c00008e
-- 2023-06-02T17:43:05.774+0000
-- # write your SQL statement here: you are given a table 'removeexclamationmarks' with column 's'
-- return a table with column 's' and your result in a column named 'res'.
SELECT s, REPLACE(s, '!', '') AS res
FROM removeexclamationmarks