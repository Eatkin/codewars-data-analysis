// https://www.codewars.com/kata/5663f5305102699bad000056
// 2023-05-18T12:51:16.863+0000
function mxdiflg(a1, a2) {
    if (a1.length === 0 || a2.length === 0)
      return -1;
  
    a1Sorted = a1.sort((a, b) => a.length - b.length);
    a2Sorted = a2.sort((a, b) => a.length - b.length);
    return Math.max(Math.abs(a1Sorted[0].length - a2Sorted[a2.length - 1].length), Math.abs(a2Sorted[0].length - a1Sorted[a1.length - 1].length));
}