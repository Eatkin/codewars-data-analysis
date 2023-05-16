// https://www.codewars.com/kata/56269eb78ad2e4ced1000013
2023-05-09T05:53:33.392+0000
function findNextSquare(sq) {
  // Return the next square if sq is a perfect square, -1 otherwise
  if (sq === 0)
    return 1;
  if (sq === 1)
    return 4
  
  root = Math.sqrt(sq);
  if (root === Math.floor(root))
    return (root + 1) ** 2;
  
  return -1
}