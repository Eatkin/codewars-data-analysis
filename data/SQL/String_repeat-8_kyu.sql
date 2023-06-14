-- https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
-- 2023-06-02T17:42:03.659+0000
--# write your SQL statement here: you are given a table 'repeatstr' with columns 'n' and 's'
-- return a table with all columns and your result in a column named 'res'.
SELECT s, n,
REPEAT(s, n) AS res
FROM repeatstr