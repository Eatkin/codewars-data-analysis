-- https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
-- 2023-06-02T17:09:17.446+0000
SELECT GREATEST(s1, s2, s3, s4) AS res
FROM  (
  SELECT
  a + b + c AS s1,
  a * (b + c) AS s2,
  (a + b) * c AS s3,
  a * b * c AS s4
  FROM expression_matter
) AS blah