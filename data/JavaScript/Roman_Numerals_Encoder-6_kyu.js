// https://www.codewars.com/kata/51b62bf6a9c58071c600001b
// 2023-06-01T14:39:20.144+0000
const numerals = {
  1: "I",
  4: "IV",
  5: "V",
  9: "IX",
  10: "X",
  40: "XL",
  50: "L",
  90: "XC",
  100: "C",
  400: "CD",
  500: "D",
  900: "CM",
  1000: "M"
}

function solution(number){
  let keys = Object.keys(numerals).reverse();
  let numeral_representation = "";
  for (let i = 0; i < keys.length; i++) {
    let value = keys[i]
    let count = Math.floor(number / value);
    numeral_representation += numerals[value].repeat(count);
    number -= value * count;
  }
  
  return numeral_representation;
}