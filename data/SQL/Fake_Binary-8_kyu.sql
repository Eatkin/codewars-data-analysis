-- https://www.codewars.com/kata/57eae65a4321032ce000002d
-- 2023-05-03T07:35:18.381+0000
DO $$ 
BEGIN
  IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'fakebin' AND column_name = 'res') THEN
    ALTER TABLE fakebin ADD res TEXT;
  END IF;
END $$;

UPDATE fakebin SET res = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(x, '1', '0'), '2', '0'), '3', '0'), '4', '0'), '5', '1'), '6', '1'), '7', '1'), '8', '1'), '9', '1');

SELECT x, res FROM fakebin;