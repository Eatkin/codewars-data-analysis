% https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
% 2023-05-20T16:48:12.578+0000
quarter_of(Month, Quarter) :-
  Month =< 3,
  Quarter is 1.
  
quarter_of(Month, Quarter) :-
  Month > 3,
  Month =< 6,
  Quarter is 2.
  
quarter_of(Month, Quarter) :-
  Month > 6,
  Month =< 9,
  Quarter is 3.
  
quarter_of(Month, Quarter) :-
  Month > 9,
  Month =< 12,
  Quarter is 4.