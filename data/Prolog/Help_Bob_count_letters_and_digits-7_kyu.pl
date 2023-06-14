% https://www.codewars.com/kata/5738f5ea9545204cec000155
% 2023-05-20T16:59:16.384+0000
count_letters_and_digits(Input, Result) :-
    string_chars(Input, Chars),
    count_letters_and_digits_helper(Chars, 0, Result).

count_letters_and_digits_helper([], Count, Count).

count_letters_and_digits_helper([Char|Rest], Count, Result) :-
    (char_type(Char, alpha) ; char_type(Char, digit)),
    NewCount is Count + 1,
    count_letters_and_digits_helper(Rest, NewCount, Result).
    
count_letters_and_digits_helper([_|Rest], Count, Result) :-
    count_letters_and_digits_helper(Rest, Count, Result).