-- https://www.codewars.com/kata/55cbc3586671f6aa070000fb
-- 2023-06-02T18:28:11.863+0000
-- you will be given a table 'kata' with columns 'id', 'base', and 'factor'. 
-- return the 'id' and your result in a column named 'res'.
SELECT id,
CASE
  WHEN base % factor = 0 THEN true
  ELSE false
END AS res
FROM kata