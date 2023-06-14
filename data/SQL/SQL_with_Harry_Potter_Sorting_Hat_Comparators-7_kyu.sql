-- https://www.codewars.com/kata/5abcf0f930488ff1a6000b66
-- 2023-06-03T14:51:43.897+0000
/* Oh you may not think I'm pretty,
But don't judge on what you see,
I'll eat myself if you can find
A smarter hat than me. */
SELECT * FROM students
WHERE (quality1 = 'evil' AND quality2 = 'cunning') OR (quality1 = 'cunning' AND quality2 = 'evil')
OR (quality1 = 'brave' AND quality2 != 'evil')
OR quality1 = 'studious'
OR quality2 = 'intelligent'
OR quality1 = 'hufflepuff'
OR quality2 = 'hufflepuff'