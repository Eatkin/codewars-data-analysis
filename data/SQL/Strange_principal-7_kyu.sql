-- https://www.codewars.com/kata/55fc061cc4f485a39900001f
-- 2023-05-06T12:05:26.870+0000
-- # write your SQL statement here: you are given a table 'numofopenlockers' with column 'n',
-- return a table with column 'n' and your result in a column named 'res'.

SELECT n,
CAST(FLOOR(SQRT(n)) AS INT) AS res
FROM numofopenlockers;