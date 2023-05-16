// https://www.codewars.com/kata/55d24f55d7dd296eb9000030
2023-03-09T10:59:10.563+0000
var summation = function (num) {
  return (num > 1)  ? num + summation(num - 1) : 1;
}