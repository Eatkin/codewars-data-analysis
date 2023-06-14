// https://www.codewars.com/kata/5680781b6b7c2be860000036
// 2023-06-02T09:48:58.050+0000
function vowelIndices(word){
  let letters = Array.from(word);
  let indices = [];
  let vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  letters.forEach((char, i) => {
    if (vowels.includes(char.toLowerCase()))
      indices.push(i + 1);
  });
  return indices;
}