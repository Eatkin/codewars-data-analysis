// https://www.codewars.com/kata/5848565e273af816fb000449
// 2023-06-02T10:01:55.321+0000
var encryptThis = function(text) {
  let encryptWord = function(word) {
    let len = word.length;
    if (len === 0)
      return "";
    if (len === 1)
      return word.charCodeAt(0).toString();
    if (len === 2)
      return word.charCodeAt(0).toString() + word.slice(1);
    if (len == 3)
      return word.charCodeAt(0).toString() + word.slice(-1) + word.slice(1, 2);
    return word.charCodeAt(0).toString() + word.slice(-1) + word.slice(2, -1) + word.slice(1, 2);
  }
  let arr = text.split(" ");
  arr = arr.map(encryptWord);
  return arr.join(" ");
}