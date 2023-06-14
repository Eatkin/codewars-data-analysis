% https://www.codewars.com/kata/55f2b110f61eb01779000053
% 2023-05-22T11:56:50.353+0000
get_sum(A, B, Result) :-
  (A < B) ->
  get_sum_helper(A, B, 0, Result)
  ;
  get_sum_helper(B, A, 0, Result).
  
get_sum_helper(Current, End, Acc, Result) :-
  Current =< End,
  NewAcc is Acc + Current,
  Next is Current + 1,
  get_sum_helper(Next, End, NewAcc, Result).
  
get_sum_helper(Current, End, Acc, Acc) :-
  Current > End.