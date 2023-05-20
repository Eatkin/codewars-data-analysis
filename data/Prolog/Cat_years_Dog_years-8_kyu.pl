% https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
% 2023-05-19T17:16:54.574+0000
% first year
human_years_cat_years_dog_years(HY, [H, C, D]) :-
    HY =:= 1,
    H = 1,
    C = 15,
    D = 15.

% second year
human_years_cat_years_dog_years(HY, [H, C, D]) :-
    HY =:= 2,
    H = 2,
    C = 24,
    D = 24.

% every subsequent year
human_years_cat_years_dog_years(HY, [H, C, D]) :-
    HY > 2,
    H = HY,
    C is 24 + (HY - 2) * 4,
    D is 24 + (HY - 2) * 5.
