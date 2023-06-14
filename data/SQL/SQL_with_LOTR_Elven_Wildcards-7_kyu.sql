-- https://www.codewars.com/kata/5ad90fb688a0b74111000055
-- 2023-06-03T09:35:11.057+0000
--but on the land of Lórien no shadow lay--
SELECT INITCAP(firstname) || ' ' || INITCAP(lastname) AS shortlist
FROM Elves
WHERE firstname LIKE '%tegil%'
OR lastname LIKE '%astar%'