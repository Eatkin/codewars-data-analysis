// https://www.codewars.com/kata/53697be005f803751e0015aa
// 2023-06-02T09:34:42.602+0000
const substitutions = {
  "a": "1",
  "e": "2",
  "i": "3",
  "o": "4",
  "u": "5",
  "1": "a",
  "2": "e",
  "3": "i",
  "4": "o",
  "5": "u"
}
function encode(string) {
  const regex = /[aeiou]/g;
  return string.replace(regex, match => substitutions[match]);
}

function decode(string) {
  const regex = /[12345]/g;
  return string.replace(regex, match => substitutions[match]);
}