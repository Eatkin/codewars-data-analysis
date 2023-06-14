-- https://www.codewars.com/kata/554e4a2f232cdd87d9000038
-- 2023-06-02T19:33:59.783+0000
--# write your SQL statement here: you are given a table 'dnastrand' with column 'dna'
-- return a table with column 'dna' and your result in a column named 'res'.
SELECT dna,
TRANSLATE(dna, 'ACTG', 'TGAC') AS res
FROM dnastrand