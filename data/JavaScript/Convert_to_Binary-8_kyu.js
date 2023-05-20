// https://www.codewars.com/kata/59fca81a5712f9fa4700159a
// 2023-05-18T10:43:03.880+0000
function toBinary(n){
  if (n === 0)
    return 0;
  
  binaryString = "";
  while (n > 0) {
    binaryString = String(n&1) + binaryString;
    n = n >> 1;
  }
  return parseInt(binaryString);
}