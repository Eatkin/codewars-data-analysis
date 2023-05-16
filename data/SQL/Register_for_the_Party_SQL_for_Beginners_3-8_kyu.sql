-- https://www.codewars.com/kata/590cc86f7557c0494000007e
-- 2023-05-03T08:15:07.119+0000
INSERT INTO participants ("name", age)
VALUES ('Ed', 31);

UPDATE participants
SET attending =
  CASE
    WHEN age >= 21 THEN
      true
    ELSE
      false
  END;
      

SELECT * FROM participants;
