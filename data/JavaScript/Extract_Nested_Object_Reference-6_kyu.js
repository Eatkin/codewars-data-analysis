// https://www.codewars.com/kata/527a6e602a7db3456e000a2b
// 2023-06-12T13:03:37.104+0000
// return the nested property value if it exists,
// otherwise return undefined
Object.prototype.hash = function(string) {
  let keys = string.split('.');
  let value = this;
  try {
    for (const key of keys) {
      value = value[key];
    }
    return value;
  }
  catch {
    return undefined;
  }
}