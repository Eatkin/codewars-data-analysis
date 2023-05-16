-- https://www.codewars.com/kata/583710ccaa6717322c000105
-- 2023-05-03T11:42:27.258+0000
-- # write your SQL statement here: you are given a table 'multiplication' with column 'number', return a table with column 'number' and your result in a column named 'res'.
SELECT number,
  CASE
    WHEN "number" % 2 = 0 THEN
      8 * "number"
    ELSE
      9 * "number"
  END as res
FROM multiplication;