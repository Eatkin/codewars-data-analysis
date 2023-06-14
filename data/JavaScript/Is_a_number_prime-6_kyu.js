// https://www.codewars.com/kata/5262119038c0985a5b00029f
// 2023-06-02T14:45:18.048+0000
function isPrime(num) {
  // Trivial cases
  if (num < 2)
    return false;
  
  if (num === 2)
    return true;
  
  if (num % 2 === 0)
    return false;
  
  
  for (let i = 3; i <= Math.ceil(Math.sqrt(num)); i+=2)  {
    if (num % i === 0)
      return false;
  }
  return true;
}
