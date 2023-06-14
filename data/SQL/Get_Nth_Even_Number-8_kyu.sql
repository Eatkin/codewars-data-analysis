-- https://www.codewars.com/kata/5933a1f8552bc2750a0000ed
-- 2023-06-02T17:28:54.331+0000
-- # write your SQL statement here: you are given a table 'ntheven' with column 'n'
-- return a table with column 'n' and your result in a column named 'res'.

SELECT n, (n - 1) * 2 AS res
FROM ntheven