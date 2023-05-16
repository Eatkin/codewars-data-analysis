-- https://www.codewars.com/kata/582cba7d3be8ce3a8300007c
2023-05-14T06:53:15.391+0000
SELECT 
  s.transaction_date::date as day,
  d.name AS department,
  COUNT(s.id) AS sale_count
  FROM department d
    JOIN sale s on d.id = s.department_id
  group by day, name
  order by day asc, name asc
