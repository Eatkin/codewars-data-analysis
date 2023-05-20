// https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
// 2023-05-18T13:18:37.362+0000
function revrot(str, sz) {
    if (sz <= 0 || str === "" || sz > str.length)
      return ""
  
    // Prepare the string
    str = str.slice(0, Math.floor(str.length / sz) * sz);
  
    for (let i = 0; i <= str.length - sz; i += sz) {
      let chunk = str.slice(i, i + sz);
      let sumOfCubes = chunk.split('').map(Number).map(num => Math.pow(num, 3)).reduce((sum, num) => sum + num, 0);
      if (sumOfCubes % 2 === 0)
        chunk = chunk.split('').reverse().join('');
      else
        chunk = chunk.slice(1) + chunk.slice(0, 1);
      
      // Replace the chunk
      str = str.slice(0, i) + chunk + str.slice(i + sz);
    }
  
  return str
}