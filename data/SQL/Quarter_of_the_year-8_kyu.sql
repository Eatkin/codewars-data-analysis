-- https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
-- 2023-06-02T16:30:05.567+0000
-- # write your SQL statement here: you are given a table 'quarterof' with column 'month'
-- return a table with column 'month' and your result in a column named 'res'.
SELECT month, CAST(CEIL(CAST(month AS NUMERIC) / 3) AS INT) AS res
from quarterof