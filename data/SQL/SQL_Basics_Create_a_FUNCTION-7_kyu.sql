-- https://www.codewars.com/kata/580fe518cefeff16d00000c0
-- 2023-05-06T12:15:21.643+0000
CREATE FUNCTION increment_by_one(num INT)
RETURNS INT
AS
$$
  SELECT num + 1;
$$
LANGUAGE SQL;