-- https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
-- 2023-06-02T19:13:26.623+0000
/*
the table "nums" contains an integer "n", the number
return your result in a column "res"
*/
SELECT (n ^ 3)::INTEGER as res
FROM nums