-- https://www.codewars.com/kata/57eae65a4321032ce000002d
-- 2023-05-03T07:37:59.367+0000
SELECT x, REPLACE(
  REPLACE(
    REPLACE(
      REPLACE(
        REPLACE(
          REPLACE(
            REPLACE(
              REPLACE(
                REPLACE(x, '1', '0')
                , '2', '0')
              , '3', '0')
            , '4', '0')
          , '5', '1')
        , '6', '1')
      , '7', '1')
    , '8', '1')
  , '9', '1')
as res FROM fakebin;