% https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
% 2023-05-22T11:42:00.397+0000
past(H, M, S, Result) :- 
  Result is H * 3600000 + M * 60000 + S * 1000.