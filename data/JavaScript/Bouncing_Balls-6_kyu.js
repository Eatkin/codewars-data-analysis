// https://www.codewars.com/kata/5544c7a5cb454edb3c000047
// 2023-05-18T09:56:45.791+0000
function bouncingBall(h,  bounce,  window) {
  if (!(h > 0 && bounce > 0 && bounce < 1 && window < h))
    return -1
  
  // We always see the ball on the way down
  count = 1;
  h *= bounce;
  while (h > window) {
    h *= bounce;
    count += 2; // We will see the ball on its way up and down
  }
  
  return count;
}