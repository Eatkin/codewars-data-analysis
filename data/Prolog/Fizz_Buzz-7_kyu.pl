% https://www.codewars.com/kata/5300901726d12b80e8000498
% 2023-05-22T10:31:11.952+0000
fizzify(N, Result) :-
  fizzify(N, N, [], Result).
  
fizzify(0, _, Acc, Acc).  % Base case: unify Acc with Result
  
fizzify(Current, N, Acc, Result) :-
  Current > 0,
  (
    Current mod 3 =:= 0,
    Current mod 5 =:= 0 ->
    NewElem = "FizzBuzz"
    ;
    Current mod 5 =:= 0 ->
    NewElem = "Buzz"
    ;
    Current mod 3 =:= 0 ->
    NewElem = "Fizz"
    ;
    NewElem = Current
  ),
  NewAcc = [NewElem | Acc],
  Next is Current - 1,
  fizzify(Next, N, NewAcc, Result).