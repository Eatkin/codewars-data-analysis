-- https://www.codewars.com/kata/6391fe3f322221003db3bad6
2023-05-03T14:54:59.289+0000
--# write your SQL statement here: 
-- you are given a table 'perpendicular' with column 'n'
-- return a table with this column and your result in a column named 'res'.

/*
Thought process:
[0, 1, 2, 3, 4, 5, 6, 7,  8,  9 ]
[0, 0, 1, 2, 4, 6, 9, 12, 16, 20]

f(x) = f(x - 1) + x // 2
f(3) = f(2) + 3 // 2
     = f(1) + 2 // 2 + 3 // 2
     = f(0) + 1 // 2 + 2 // 2 + 3 // 2
     = 0 + 0 + 1 + 1
f(4) = 0 + 0 + 1 + 1 + 2
f(5) = 0 + 0 + 1 + 1 + 2 + 2

f(0) = 0
f(1) = 0 + 0
f(2) = 0 + 0 + 1
f(3) = 0 + 0 + 1 + 1
f(4) = 0 + 0 + 1 + 1 + 2
f(5) = 0 + 0 + 1 + 1 + 2 + 2

Sum of first n // 2 natural numbers * 2 - (1 - n%2) * n // 2
n//2 * n // 2 + n // 2 - (1 - n % 2) * n // 2
Reduces to n // 2 * (n // 2 + n % 2)
*/

SELECT n, n / 2 * (n / 2 + n % 2) as res
FROM perpendicular;