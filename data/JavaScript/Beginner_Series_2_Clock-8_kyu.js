// https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
// 2023-03-09T11:06:06.719+0000
function past(h, m, s){
  let seconds = s + 60 * (m + 60 * h);
  return seconds * 1000;  //1s = 1000ms
}