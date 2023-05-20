// https://www.codewars.com/kata/55e2adece53b4cdcb900006c
// 2023-05-18T11:24:40.970+0000
function race(v1, v2, g) {
    if (v1 >= v2)
      return null
  
  let seconds = g/(v2 - v1) * 3600;
  let hours = Math.floor(seconds/3600);
  seconds -= hours * 3600;
  let minutes = Math.floor(seconds/60);
  seconds -= minutes * 60;
  
  return [hours, minutes, Math.floor(seconds)];
}