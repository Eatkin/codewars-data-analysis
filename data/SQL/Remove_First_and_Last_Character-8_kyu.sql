-- https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
-- 2023-06-02T18:21:59.875+0000
-- # write your SQL statement here: you are given a table 'removechar' with column 's', 
-- return a table with column 's' and your result in a column named 'res'.
SELECT s, REGEXP_REPLACE(REGEXP_REPLACE(s, '^.', ''), '.$', '') AS res
FROM removechar