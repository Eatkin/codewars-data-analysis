-- https://www.codewars.com/kata/5818d00a559ff57a2f000082
-- 2023-05-27T08:17:38.762+0000
WITH RECURSIVE pell_rec(n, prev, current) AS (
  SELECT 1, 1::BIGINT, 0::BIGINT
  UNION ALL
  SELECT n + 1, current, 2 * current + prev
  FROM pell_rec
  WHERE n < 50
)
SELECT DISTINCT pell_rec.n, current AS res
FROM pell_rec
JOIN pell
ON pell.n = pell_rec.n
ORDER BY n ASC