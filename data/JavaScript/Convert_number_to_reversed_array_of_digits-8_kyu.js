// https://www.codewars.com/kata/5583090cbe83f4fd8c000051
2023-03-10T09:11:44.810+0000
function digitize(n) {
  //code here
  n = String(n)
  let outputArray = [];
  let _len = n.length - 1;
  for (let i = _len; i >= 0; i --)
    outputArray[_len - i] = parseInt(n.charAt(i));
  
  return outputArray;
}