-- https://www.codewars.com/kata/594804a218e96caa8d00051b
-- 2023-06-05T06:54:48.575+0000
/*  SQL  */
SELECT id,
ASCII(SUBSTRING(name FROM 1 FOR 1)) AS name,
birthday,
ASCII(SUBSTRING(race FROM 1 FOR 1)) AS race
FROM demographics