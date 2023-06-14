% https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
% 2023-05-22T11:45:25.657+0000
paperwork(N, M, Result) :-
  (N >= 0, M >=0) ->
  Result is N * M
  ;
  Result is 0.