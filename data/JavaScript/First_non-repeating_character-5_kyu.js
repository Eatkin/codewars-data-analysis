// https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
// 2023-06-01T15:42:04.660+0000
function firstNonRepeatingLetter(s) {
  if (!s)
    return '';
  
  let letter_cache = [];
  let singles = [];
  [...s].forEach((c, i) => {
    if (!letter_cache.includes(c.toLowerCase())) {
      letter_cache.push(c.toLowerCase());
      singles.push(c);
    }
    else {
      if (singles.includes(c.toLowerCase()))
        singles.splice(singles.indexOf(c.toLowerCase()), 1);
      else if (singles.includes(c.toUpperCase()))
        singles.splice(singles.indexOf(c.toUpperCase()), 1);
    }
  });
  
  return (singles.length > 0) ? singles[0] : "";
}