// https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15
// 2023-05-18T10:55:10.986+0000
function warnTheSheep(queue) {
  return (queue.indexOf("wolf") === queue.length - 1) ? "Pls go away and stop eating my sheep" : `Oi! Sheep number ${queue.length - queue.indexOf("wolf") - 1}! You are about to be eaten by a wolf!`
}