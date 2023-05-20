// https://www.codewars.com/kata/583f158ea20cfcbeb400000a
// 2023-05-18T08:06:37.076+0000
let operators = {
  "add": "+",
  "subtract": "-",
  "multiply": "*",
  "divide": "/"
};

function arithmetic(a, b, operator){
  // Awful solution, never do this
  return eval(a + operators[operator] + b);
}