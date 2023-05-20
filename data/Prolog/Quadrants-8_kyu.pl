% https://www.codewars.com/kata/643af0fa9fa6c406b47c5399
% 2023-05-19T19:56:03.509+0000
quadrant(X, Y, Q) :-
  X > 0,
  Y > 0,
  Q is 1.
  
quadrant(X, Y, Q) :-
  X < 0,
  Y > 0,
  Q is 2.

quadrant(X, Y, Q) :-
  X < 0,
  Y < 0,
  Q is 3.
 
quadrant(X, Y, Q) :-
  X > 0,
  Y < 0,
  Q is 4.