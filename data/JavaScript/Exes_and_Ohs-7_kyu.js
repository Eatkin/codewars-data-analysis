// https://www.codewars.com/kata/55908aad6620c066bc00002a
2023-03-10T11:40:16.708+0000
function XO(str) {
    //code here
  str = str.toLowerCase();
  let _len = str.length;
  let x_count = 0;
  let o_count = 0;
  for (let i = 0; i < _len; i++)  {
    let _char = str.charAt(i);
    if (_char === "x")
      x_count++;
    else if (_char == "o")
      o_count++;
  }
  
  return x_count == o_count;
}