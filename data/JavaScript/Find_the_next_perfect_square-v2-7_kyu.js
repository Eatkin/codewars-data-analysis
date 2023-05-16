// https://www.codewars.com/kata/56269eb78ad2e4ced1000013
2023-05-10T05:31:36.232+0000
function findNextSquare(sq) {
  // Return the next square if sq is a perfect square, -1 otherwise
  if (sq == 0)
    return 1;
  if (sq == 1)
    return 4;

  let left = 0;
  let right = Math.trunc(sq / 2);
  while (left <= right) {
    let mid = Math.trunc((right + left) / 2);
    let square = mid ** 2;
    if (square == sq)
      return (mid + 1) ** 2;
    if (square > sq)
      right = mid - 1;
    else
      left = mid + 1;
  }
  
  return -1
}