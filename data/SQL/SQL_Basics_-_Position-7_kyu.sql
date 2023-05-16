-- https://www.codewars.com/kata/59401e0e54a655a298000040
-- 2023-05-05T08:11:23.454+0000
/*  SQL  */

SELECT id, name,
POSITION(',' IN characteristics) AS comma
FROM monsters
ORDER BY comma ASC;