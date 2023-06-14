% https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6
% 2023-05-22T12:08:56.392+0000
cockroach_speed(Speed, Result) :-
  Result is floor(Speed * 100000 / 3600).