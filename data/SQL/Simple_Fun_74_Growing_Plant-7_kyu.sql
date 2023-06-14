-- https://www.codewars.com/kata/58941fec8afa3618c9000184
-- 2023-06-03T08:01:15.660+0000
WITH RECURSIVE plant_growth(id, day, plant_height, up_speed, down_speed, desired_height) AS (
  SELECT ROW_NUMBER() OVER (), 1, up_speed, up_speed, down_speed, desired_height
  FROM growing_plant
  UNION ALL
  SELECT plant_growth.id, plant_growth.day + 1, plant_growth.plant_height + up_speed - down_speed, up_speed, down_speed, desired_height
  FROM plant_growth
  WHERE plant_growth.plant_height < desired_height
)
SELECT id,
day AS num_days
FROM plant_growth
WHERE plant_height >= desired_height
ORDER BY id