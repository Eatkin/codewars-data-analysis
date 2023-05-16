-- https://www.codewars.com/kata/5a023c426975981341000014
-- 2023-05-05T08:12:49.491+0000
--# write your SQL statement here: 
-- you are given a table 'otherangle' with columns 'a' and 'b'.
-- return a table with these columns and your result in a column named 'res'.

SELECT a, b, 180 - a - b AS res
FROM otherangle