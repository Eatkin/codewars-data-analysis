-- https://www.codewars.com/kata/523b623152af8a30c6000027
-- 2023-06-02T18:36:38.186+0000
--# write your SQL statement here: 
-- you are given a table 'square' with column 'n'
-- return a table with:
--   this column and your result in a column named 'res'
SELECT n, (n ^ 2)::INTEGER AS res
FROM square