// https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1
// 2023-06-01T17:19:18.197+0000
function arrayMadness(a, b) {
  if (a.map(x => x ** 2).reduce((sum, i) => sum + i, 0) > b.map(x => x ** 3).reduce((sum, i) => sum + i, 0))
    return true;
  
  return false;
}