-- https://www.codewars.com/kata/5adadcb36edb07df5600092e
-- 2023-05-27T15:47:22.666+0000
-- # write your SQL statement here: 
-- you are given a table 'seven_wonders_science' with columns 'id', 'compasses', 'gears' and 'tablets'
-- return a table with columns 'id', 'compasses', 'gears' and 'tablets' and your result in a column named 'res'
SELECT id, compasses, gears, tablets,
LEAST(compasses, gears, tablets) * 7 + compasses * compasses + gears * gears + tablets * tablets AS res
FROM seven_wonders_science