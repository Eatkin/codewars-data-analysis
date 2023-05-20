// https://www.codewars.com/kata/5761a717780f8950ce001473
// 2023-05-18T18:36:55.436+0000
function  calculateAge(birthYear, targetYear) {
   let diff = Math.abs(birthYear - targetYear);
   if (birthYear === targetYear)
     return "You were born this very year!";
   if (targetYear === birthYear + 1)
     return "You are 1 year old.";
   if (targetYear > birthYear)
     return `You are ${diff} years old.`;
   if (targetYear + 1 === birthYear)
     return "You will be born in 1 year.";
   
  return `You will be born in ${diff} years.`
}

