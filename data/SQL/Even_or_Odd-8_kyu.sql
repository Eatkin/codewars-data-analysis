-- https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
-- 2023-06-02T18:38:32.438+0000
SELECT number, 
CASE
  WHEN number % 2 = 0 THEN 'Even'
  ELSE 'Odd'
END AS is_even
FROM numbers