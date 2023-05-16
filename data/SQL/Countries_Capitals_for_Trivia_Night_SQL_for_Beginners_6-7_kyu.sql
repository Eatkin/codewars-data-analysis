-- https://www.codewars.com/kata/5e5f09dc0a17be0023920f6f
-- 2023-05-03T08:24:34.378+0000
SELECT capital FROM countries
WHERE (continent = 'Africa' OR continent = 'Afrika') AND (country LIKE 'E%')
ORDER BY capital ASC
LIMIT 3;