-- https://www.codewars.com/kata/59342039eb450e39970000a6
-- 2023-06-02T17:27:42.980+0000
-- # write your SQL statement here: you are given a table 'oddcount' with column 'n', return a table with column 'n' and your result in a column named 'res'.
SELECT n, n / 2 AS res
FROM oddcount