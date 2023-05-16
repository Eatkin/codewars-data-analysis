// https://www.codewars.com/kata/56676e8fabd2d1ff3000000c
2023-03-09T12:20:24.764+0000
function findNeedle(haystack) {
  return "found the needle at position " + haystack.findIndex(elem => elem === "needle")
}