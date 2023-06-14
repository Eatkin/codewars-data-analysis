-- https://www.codewars.com/kata/5802e32dd8c944e562000020
-- 2023-05-26T19:05:48.750+0000
SELECT products.*, companies.name AS company_name FROM products
JOIN companies ON products.company_id = companies.id