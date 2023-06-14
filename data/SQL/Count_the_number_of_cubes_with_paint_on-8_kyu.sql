-- https://www.codewars.com/kata/5763bb0af716cad8fb000580
-- 2023-06-02T17:54:23.121+0000
--# write your SQL statement here: 
-- you are given a table 'squares' with column 'n' (numer of cubes).
-- return a table with:
--   this column and your result in a column named 'res'
SELECT n,
CASE
  WHEN n = 0 THEN 1
  ELSE ((n + 1) ^ 3 - (n - 1) ^ 3)::INTEGER
END AS res
FROM squares