// https://www.codewars.com/kata/5503013e34137eeeaa001648
// 2023-05-18T09:21:45.385+0000
function diamond(n){
  if (n % 2 === 0 || n < 0)
    return null;
  // Construct a diamond
  diamond_arr = [];
  upper = Math.floor(n / 2);
  for (let i = 0; i < upper; i++)
    diamond_arr.push(" ".repeat(upper - i) + "*".repeat(i * 2 + 1) + "\n");
  
  diamond_arr.push("*".repeat(n) + "\n");

  // Now construct the bottom half of the diamond
  // Slice all but the last element of the array. then reverse it and add it to the end
  diamond_arr.push(...diamond_arr.slice(0, -1).reverse());
  return diamond_arr.join('');
}