// https://www.codewars.com/kata/523b4ff7adca849afe000035
2023-03-09T12:58:55.478+0000
const greet = function()  {
  let greeting = "";
  while (greeting != "hello world!")  {
    greeting = "h".repeat(Math.ceil(Math.random() * 5));
    greeting += "e".repeat(Math.ceil(Math.random() * 5));
    greeting += "l".repeat(Math.ceil(Math.random() * 5));
    greeting += "o".repeat(Math.ceil(Math.random() * 5));
    greeting += " ".repeat(Math.ceil(Math.random() * 5));
    greeting += "w".repeat(Math.ceil(Math.random() * 5));
    greeting += "o".repeat(Math.ceil(Math.random() * 5));
    greeting += "r".repeat(Math.ceil(Math.random() * 5));
    greeting += "l".repeat(Math.ceil(Math.random() * 5));
    greeting += "d".repeat(Math.ceil(Math.random() * 5));
    greeting += "!".repeat(Math.ceil(Math.random() * 5));
    }
  return greeting;
}