// https://www.codewars.com/kata/52de553ebb55d1fca3000371
// 2023-06-02T10:44:14.478+0000
var findMissing = function (list) {  
  // We have to iterate over minimum the first 3 elements
  let diff = 1000000; // Arbitrarily large
  for (let i = 1; i < 3; i++) {
    // Negative progressions need accounting for
    diff = Math.min(Math.abs(list[i] - list[i - 1]), Math.abs(diff));
    diff *= Math.sign(list[i] - list[i - 1]);
  }
  // Now we know what each term should be
  for (let i = 1; i < list.length; i++) {
    if (list[i] - list[i - 1] != diff)
        return list[i] - diff;
  }
}