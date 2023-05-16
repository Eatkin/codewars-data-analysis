-- https://www.codewars.com/kata/5168bb5dfe9a00b126000018
2023-05-05T18:03:27.482+0000
-- # write your SQL statement here: you are given a table 'solution' with column 'str', return a table with column 'str' and your result in a column named 'res'.
SELECT str,
REVERSE(str) as res
FROM solution;