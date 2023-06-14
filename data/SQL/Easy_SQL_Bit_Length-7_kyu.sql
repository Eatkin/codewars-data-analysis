-- https://www.codewars.com/kata/594900e16fd782a607000059
-- 2023-06-05T07:06:40.398+0000
/*  SQL  */
SELECT id,
BIT_LENGTH(name) AS name,
birthday,
BIT_LENGTH(race) AS race
FROM demographics