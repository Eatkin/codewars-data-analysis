% https://www.codewars.com/kata/563e320cee5dddcf77000158
% 2023-05-25T18:15:53.062+0000
get_average(List, Res) :-
  sum_list(List, Sum),
  count_elements(List, Elements),
  Res is Sum // Elements.

sum_list([], 0).

sum_list([Num | List], Sum) :-
  sum_list(List, RestSum),
  Sum is RestSum + Num.
  
count_elements([], 0).

count_elements([Elem | List], Elements) :-
  count_elements(List, RestElements),
  Elements is RestElements + 1.