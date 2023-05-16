// https://www.codewars.com/kata/58649884a1659ed6cb000072
// 2023-03-09T14:31:18.305+0000
function updateLight(current) {
  const lights = ["green", "yellow", "red"];
  return lights[(lights.indexOf(current) + 1) % lights.length]
}