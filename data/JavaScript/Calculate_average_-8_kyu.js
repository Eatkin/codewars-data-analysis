// https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
// 2023-05-18T10:37:39.050+0000
function findAverage(array) {
  return (array.length) ? array.reduce((i, n) => i + n, 0) / array.length : 0;
}