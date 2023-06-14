% https://www.codewars.com/kata/55edaba99da3a9c84000003b
% 2023-05-25T18:04:57.615+0000
divisible_by([], _, []).

divisible_by([Number | Rest], Divisor, [Number | Result]) :- 
  0 is Number mod Divisor,
  divisible_by(Rest, Divisor, Result).
  
divisible_by([_|Rest], Divisor, Result) :-
  divisible_by(Rest, Divisor, Result).