-- https://www.codewars.com/kata/5942b066db68b6f35f000084
-- 2023-06-05T06:22:38.566+0000
/*  SQL  */
SELECT project, commits, contributors,
REGEXP_REPLACE(address, '[[:digit:]]', '!', 'g') AS address
FROM repositories