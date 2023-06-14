// https://www.codewars.com/kata/56747fd5cb988479af000028
// 2023-06-12T13:07:10.863+0000
function getMiddle(s)
{
  return (s.length % 2 == 0) ? s.substr(Math.floor(s.length / 2) - 1, 2) :  s.substr((s.length + 1) / 2 - 1, 1);
}