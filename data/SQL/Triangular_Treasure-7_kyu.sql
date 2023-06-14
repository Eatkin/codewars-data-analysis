-- https://www.codewars.com/kata/525e5a1cb735154b320002c8
-- 2023-05-27T10:57:46.861+0000
--# write your SQL statement here: 
-- you are given a table 'triangular' with column 'n'
-- return a table with this column and your result in a column named 'res'.
SELECT n,
CASE
  WHEN n <= 0 THEN
    0
  ELSE
    CAST(0.5 * (n * n + n) AS BIGINT)
  END res
FROM triangular