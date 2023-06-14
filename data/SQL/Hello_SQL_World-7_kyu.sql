-- https://www.codewars.com/kata/581283eb0a5fb13e06000020
-- 2023-05-20T17:15:58.306+0000
CREATE TABLE hello_world (
  "Greeting" TEXT
);

INSERT INTO hello_world ("Greeting")
VALUES ('hello world!');

SELECT "Greeting" FROM hello_world;