-- https://www.codewars.com/kata/59413d53f5c3947364000016
2023-05-05T18:09:06.611+0000
/*  SQL  */
SELECT regexp_split_to_table(text, '[aeiouAEIOU]') AS results
FROM random_string