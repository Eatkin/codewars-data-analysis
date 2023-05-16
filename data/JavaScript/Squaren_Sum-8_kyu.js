// https://www.codewars.com/kata/515e271a311df0350d00000f
// 2023-03-09T10:46:28.417+0000
function squareSum(numbers){
  sum = 0;
  numbers.forEach(function(num) {
    sum += num ** 2
  });
  return sum;
}