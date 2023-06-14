-- https://www.codewars.com/kata/5d50e3914861a500121e1958
-- 2023-06-03T09:03:52.750+0000
SELECT 
CASE
  WHEN CHR(((SUM(character) - 1) % 26 + 97)::INT) IS NULL THEN 'z'
  ELSE CHR(((SUM(character) - 1) % 26 + 97)::INT)
END AS letter
FROM (
  SELECT ASCII(UNNEST(string_to_array(letter, NULL))) - 96
  AS character
  FROM letters
) AS subquery;