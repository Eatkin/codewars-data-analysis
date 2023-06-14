// https://www.codewars.com/kata/55d277882e139d0b6000005d
// 2023-06-02T14:59:30.744+0000
var findAverage = function (nums) {
  return nums.reduce((a, e) => a + e) / nums.length;
}