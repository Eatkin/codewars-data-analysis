-- https://www.codewars.com/kata/5943b797d8c9432eb7000066
-- 2023-06-05T07:00:58.084+0000
/*  SQL  */
SELECT RPAD(md5, LENGTH(sha256), '1') AS md5,
LPAD(sha1, LENGTH(sha256), '0') AS sha1,
sha256
FROM encryption