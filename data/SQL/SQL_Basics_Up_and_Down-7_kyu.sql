-- https://www.codewars.com/kata/595a3ba3843b0cbf8e000004
-- 2023-06-04T20:01:20.379+0000
/*  SQL  */
SELECT
CASE
  WHEN SUM(number1) % 2 = 1 THEN MIN(number1)
  ELSE MAX(number1)
END AS number1,
CASE
  WHEN SUM(number2) % 2 = 1 THEN MIN(number2)
  ELSE MAX(number2)
END AS number2
FROM numbers
LIMIT 1