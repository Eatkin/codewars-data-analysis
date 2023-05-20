-- https://www.codewars.com/kata/5db5ff03d10bfa001da9cf2e
-- 2023-05-19T08:06:49.225+0000
SELECT id,
network(ip_address) AS first_address,
broadcast(ip_address) AS last_address
FROM connections
ORDER BY id ASC;