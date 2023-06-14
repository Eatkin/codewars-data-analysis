-- https://www.codewars.com/kata/52fba66badcd10859f00097e
-- 2023-06-02T18:59:05.800+0000
-- # write your SQL statement here: you are given a table 'disemvowel' with column 'str'
-- return a table with column 'str' and your result in a column named 'res'.
SELECT str,
-- This is really dumb but it works
REPLACE(
  REPLACE(
    REPLACE(
      REPLACE(
        REPLACE(
          REPLACE(
            REPLACE(
              REPLACE(
                REPLACE(
                  REPLACE(str, 'a', '')
                  , 'e', '')
                , 'i', '')
              , 'o', '')
            , 'u', '')
          , 'A', '')
        , 'E', '')
      , 'I', '')
    , 'O', '')
  , 'U', '') AS res
FROM disemvowel