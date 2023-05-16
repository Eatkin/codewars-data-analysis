// https://www.codewars.com/kata/563b662a59afc2b5120000c6
2023-03-10T13:53:14.706+0000
function nbYear(p0, percent, aug, p) {
    // your code
  let years = 0;
  while (p0 < p)  {
    p0 *= (1 + percent * 0.01);
    p0 += aug;
    p0 = Math.floor(p0);
    years++;
  }
  return years;
}