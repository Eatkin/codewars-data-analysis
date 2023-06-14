// https://www.codewars.com/kata/526571aae218b8ee490006f4
// 2023-06-01T14:52:47.839+0000
let powers_of_two = {
  0: 1
};

var countBits = function(n) {
  let exponent = 0;
  let value = 2 ** exponent;
  while (value < n) {
    value *= 2;
    exponent++;
    powers_of_two[exponent] = value;
  };
  
  
  let bits = 0;
  while (exponent >= 0) {
    if (n - powers_of_two[exponent] >= 0)  {
      bits++;
      n -= powers_of_two[exponent];
    }
    exponent--;
  };
  return bits;
};