-- https://www.codewars.com/kata/6357825a00fba284e0189798
-- 2023-06-02T20:55:02.569+0000
--# write your SQL statement here: 
-- you are given a table 'trianglesum' with column 'n' (the bounds in SQL translation: 0 <= n <= 10^5)
-- return a table with this column and your result in a column named 'res'.
SELECT n,
((n + 1) * (n^2 + 2*n + 1) - n * (n + 1) * (2 * n + 1) / 6)::BIGINT AS res
FROM trianglesum
-- Blathering notes just incase anybody wants to read them, this took me HOURS to work out
-- n = 0:
-- 1
-- n = 1:
-- 1 2
--   4
-- n = 2:
-- 1 2 3
--   4 5
--     7
-- n = 3:
-- 1 2 3 4
--   4 5 6
--     7 8
--       10
-- The diag is 1, 4, 7, 10 i.e. row*3 + 1
-- Should I be summing diags?

-- so we start with n = 2:
-- n + 1, n + 1 + 4, n + 1 + 4 + 5
-- grouping (n + 1) * (n + 1) + (n + 2) * n + (n + 3) * (n - 1)
-- n = 3:
-- n +1, n + 1 + 5, n + 1 + 5 + 6, n + 1 + 5 + 6 + 7
-- grouping (n + 1) * (n + 1) + 5 * n + 6 * (n - 1) + 7
-- (n + 1) * (n + 1) + (n + 2) * n + (n + 3) * (n - 1) + (n + 4) * (n - 2)
-- from x = 0 to n:
-- (n + 1 + x) * (n + 1 - x) = n ^ 2 + n + n + 1 - x^2
-- reduces to n^2 + 2n + 1 - x^2
-- This is still summed from 0 to n
-- so we need (n + 1) * (n^2 + 2n + 1) - the sum of the first n squares