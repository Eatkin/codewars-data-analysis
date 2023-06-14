// https://www.codewars.com/kata/5704aea738428f4d30000914
// 2023-06-02T11:52:41.403+0000
function tripleTrouble(one, two, three){
  let combined_string = "";
  for (let i = 0; i < one.length; i++) {
    combined_string += one[i] + two[i] + three[i];
  }
  return combined_string;
 }