-- https://www.codewars.com/kata/522551eee9abb932420004a0
-- 2023-05-07T15:00:36.789+0000
--# write your SQL statement here: 
-- you are given a table 'fibo' with column 'n'.
-- return a table with:
--   this column and your result in a column named 'res'
--   ordered ascending by 'n'
--   distinct results (remove duplicates)

WITH RECURSIVE fib(n, prev, current) AS (
  VALUES (1, 1::BIGINT, 0::BIGINT)
  UNION ALL
  SELECT n + 1, current, prev + current FROM fib WHERE n < 51
)
SELECT DISTINCT fibo.n, fib.current AS res
FROM fibo
JOIN fib on fibo.n = fib.n
ORDER BY fibo.n ASC