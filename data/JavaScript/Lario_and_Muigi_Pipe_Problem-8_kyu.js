// https://www.codewars.com/kata/56b29582461215098d00000f
// 2023-05-18T08:03:18.315+0000
function pipeFix(numbers){
  let _min = Math.min(...numbers);
  let _max = Math.max(...numbers);
  let arr = []
  for (let i = _min; i <= _max; i++)
    arr[i - _min] = i;
  return arr
}