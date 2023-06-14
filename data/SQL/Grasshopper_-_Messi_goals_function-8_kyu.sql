-- https://www.codewars.com/kata/55f73be6e12baaa5900000d4
-- 2023-06-02T18:37:23.663+0000
-- you will be given a table, goals, with columns la_liga_goals, copa_del_rey_goals, and champions_league_goals
-- Return a table with a column, res.
SELECT la_liga_goals + copa_del_rey_goals + champions_league_goals AS res
FROM goals
