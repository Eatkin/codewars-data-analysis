-- https://www.codewars.com/kata/55d24f55d7dd296eb9000030
-- 2023-06-02T18:35:53.953+0000
-- # write your SQL statement here: you are given a table 'kata' with a column 'n'
-- return a table with 'n' and your result stored in a column naed 'res'.
SELECT n, (n * (n + 1) * 0.5)::INTEGER AS res
FROM kata