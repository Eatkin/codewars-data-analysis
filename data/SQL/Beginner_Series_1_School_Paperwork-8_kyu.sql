-- https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
-- 2023-06-02T18:24:54.233+0000
-- # write your SQL statement here: you are given a table 'paperwork' with columns 'id', n' and 'm'
-- return a table with columns 'n', 'm' and your result in a column named 'res'.
SELECT n, m,
CASE
  WHEN n > 0 AND m > 0 THEN n * m
  ELSE 0
END AS res
FROM paperwork