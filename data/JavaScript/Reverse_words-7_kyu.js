// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
// 2023-03-10T16:59:34.322+0000
function reverseWords(str) {
  // Split by space
  let words = str.split(/\s/g);
  for (let i = 0; i < words.length; i++)
      words[i] = words[i].split("").reverse().join("")

  return words.join(" ")
}