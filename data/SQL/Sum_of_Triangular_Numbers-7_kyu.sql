-- https://www.codewars.com/kata/580878d5d27b84b64c000b51
-- 2023-05-03T19:18:38.728+0000
--# write your SQL statement here: 
-- you are given a table 'sumtriangular' with column 'n'
-- return a table with this column and your result in a column named 'res'.

SELECT n, 
CASE
  WHEN n >= 0 THEN
    (n * (n + 1) * (2 * n + 1) / 6 + n * (n + 1) / 2) / 2
  ELSE
    0
END AS res
FROM sumtriangular;