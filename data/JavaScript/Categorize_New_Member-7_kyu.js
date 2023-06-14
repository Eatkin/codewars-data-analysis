// https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
// 2023-06-02T09:39:11.680+0000
function openOrSenior(data){
  return data.map(datum => {
    if (datum[0] >= 55 && datum[1] >7 )
      return "Senior";
    else
      return "Open";
  });
}