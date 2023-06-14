-- https://www.codewars.com/kata/5ac698cdd325ad18a3000170
-- 2023-06-03T10:40:09.952+0000
--- 3, 2, 1, fight! ---
SELECT f.name, SUM(f.won) AS won, SUM(f.lost) AS lost
FROM (
  SELECT fighters.name, fighters.won, fighters.lost
  FROM fighters
  JOIN winning_moves
  ON fighters.move_id = winning_moves.id
  WHERE winning_moves.move != 'Hadoken' AND winning_moves.move != 'Shouoken' AND winning_moves.move != 'Kikoken'
) AS f
GROUP BY f.name
ORDER BY won DESC
LIMIT 6