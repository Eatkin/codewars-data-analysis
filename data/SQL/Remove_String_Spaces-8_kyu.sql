-- https://www.codewars.com/kata/57eae20f5500ad98e50002c5
-- 2023-06-02T17:38:36.170+0000
-- # write your SQL statement here: you are given a table 'nospace' with column 'x'
-- return a table with column 'x' and your result in a column named 'res'.
SELECT x, REPLACE(x, ' ', '') AS res
FROM nospace