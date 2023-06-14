-- https://www.codewars.com/kata/5816a3ecf54413a113000074
-- 2023-05-26T19:21:39.693+0000
SELECT
  month,
  COUNT(payment_id) AS total_count,
  SUM(amount) AS total_amount,
  SUM(CASE WHEN staff_id = 1 THEN 1 ELSE 0 END) AS mike_count,
  SUM(CASE WHEN staff_id = 1 THEN amount ELSE 0 END) AS mike_amount,
  SUM(CASE WHEN staff_id = 2 THEN 1 ELSE 0 END) AS jon_count,
  SUM(CASE WHEN staff_id = 2 THEN amount ELSE 0 END) AS jon_amount
FROM (
  SELECT
    payment_id,
    amount,
    EXTRACT(MONTH FROM payment_date) AS month,
    staff_id
  FROM payment
) AS subquery
GROUP BY month
ORDER BY month;