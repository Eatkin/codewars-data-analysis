// https://www.codewars.com/kata/554b4ac871d6813a03000035
2023-03-10T19:24:45.517+0000
function highAndLow(numbers){
  numbers = numbers.split(" ");
  numbers = numbers.map(num => parseInt(num));
  return String(Math.max.apply(Math, numbers)) + " " + String(Math.min.apply(Math, numbers));
}