// https://www.codewars.com/kata/57202aefe8d6c514300001fd
// 2023-05-18T08:04:30.966+0000
function saleHotdogs(n){
  return (n < 5) ? n * 100 : (n < 10) ? n * 95 : n * 90;
}