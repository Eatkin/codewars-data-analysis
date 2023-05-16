# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
2023-04-22T16:12:31.860+0000
n=$1
# Sum of the first n natural numbers = 0.5n(n+1)
# Sum of first n even numbers = n(n+1)
# Sum of first n odd numbers = n(n+1) - n = n^2
# Therefore we ca calculate the sum of the nth row of the triangle by (0.5*n*(n+1))^2 - (0.5*n*(n-1))^2
# Or (0.5*n)^2 * ((n+1)^2 - (n-1)^2)
# or 0.25 * n^2 * 4n
# or n^3

echo $(($1**3))