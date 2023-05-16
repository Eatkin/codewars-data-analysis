// https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
// 2023-03-09T11:10:53.448+0000
var countSheep = function (num){
  let sheepString = "";
  for (let i = 1; i <= num; i++)
    sheepString +=  `${i} sheep...`;
  
  return sheepString;
}