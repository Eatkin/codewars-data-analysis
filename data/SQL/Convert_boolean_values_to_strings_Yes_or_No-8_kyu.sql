-- https://www.codewars.com/kata/53369039d7ab3ac506000467
2023-05-03T12:43:24.905+0000
-- # write your SQL statement here: you are given a table 'booltoword' with column 'bool', return a table with column 'bool' and your result in a column named 'res'.

SELECT "bool",
  CASE
    WHEN "bool" = true then
      'Yes'
    ELSE
      'No'
    END
  AS res
FROM booltoword