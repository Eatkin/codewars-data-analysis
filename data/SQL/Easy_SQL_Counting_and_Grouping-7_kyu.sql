-- https://www.codewars.com/kata/594633020a561e329a0000a2
2023-05-14T06:55:05.789+0000
SELECT race,
COUNT(race) AS count
FROM demographics
GROUP BY race
ORDER BY count DESC