-- https://www.codewars.com/kata/555086d53eac039a2a000083
-- 2023-06-02T18:30:16.643+0000
-- # write your SQL statement here: you are given a table 'love' with columns 'flower1' and 'flower2'
-- return a table with all the columns and your result in a column named 'res'.
SELECT flower1, flower2,
CASE
  WHEN (flower1 % 2 = 0 AND flower2 % 2 = 1) OR (flower1 % 2 = 1 AND flower2 % 2 = 0) THEN true
  ELSE false
END AS res
FROM love