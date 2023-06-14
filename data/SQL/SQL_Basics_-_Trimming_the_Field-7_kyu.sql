-- https://www.codewars.com/kata/59401c25c15cbeb58d000028
-- 2023-06-05T07:04:10.356+0000
/*  SQL  */
SELECT id,
name,
(REGEXP_MATCHES(characteristics, '^(\w*) ?,?'))[1] AS characteristic
FROM monsters
ORDER BY id