-- https://www.codewars.com/kata/5c0ae69d5f72394e130025f6
-- 2023-06-03T09:10:35.649+0000
SELECT name, greeting, (REGEXP_MATCHES(greeting, '#([0-9]+)'))[1] AS user_id
FROM greetings