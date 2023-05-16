-- https://www.codewars.com/kata/5811527d9d278b242f000006
2023-05-08T04:54:32.769+0000
CREATE VIEW departments_over_10k_sales AS (
SELECT departments.id AS id
FROM departments
JOIN sales ON departments.id = sales.department_id
JOIN products ON products.id = sales.product_id
GROUP BY departments.id
HAVING SUM(products.price) > 10000
);

CREATE VIEW members_approved_for_voucher AS (
SELECT
  members.id AS id,
  SUM(products.price) OVER (PARTITION BY sales.member_id) AS total_spending
  FROM sales
  JOIN departments_over_10k_sales ON departments_over_10k_sales.id = sales.department_id
  JOIN products ON products.id = sales.product_id
  JOIN members ON members.id = sales.member_id
);

SELECT members.id, members.name, members.email, m.total_spending
FROM members_approved_for_voucher as m
JOIN members
ON m.id = members.id
GROUP BY members.id, m.total_spending
HAVING m.total_spending > 1000
ORDER BY members.id;