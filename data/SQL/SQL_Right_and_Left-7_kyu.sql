-- https://www.codewars.com/kata/5943a58f95d5f72cb900006a
-- 2023-05-27T15:39:27.422+0000
SELECT LEFT(project, commits) AS project,
RIGHT(address, contributors) AS address
FROM repositories