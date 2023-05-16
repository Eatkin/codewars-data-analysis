-- https://www.codewars.com/kata/594257d4db68b6e99200002c
2023-05-07T15:09:59.090+0000
/*  SQL  */
SELECT project,
REGEXP_REPLACE(address, '[^a-zA-Z]+', '', 'g') AS letters,
REGEXP_REPLACE(address, '[^0-9]+', '', 'g') AS numbers
FROM repositories;