// https://www.codewars.com/kata/523b4ff7adca849afe000035
2023-03-09T11:59:34.795+0000
const greet = function() {
  let greeting = "h";
  greeting += "e".repeat(2);
  greeting = greeting.slice(0, 2);
  greeting += "l".repeat(5 + Math.ceil(Math.random() * 10));
  while (greeting != "hell")
    greeting = greeting.slice(0, -1);
  greeting += "o";
  for (let i = 0; i < 7; i++)
    greeting += " ".repeat(100 + Math.floor(Math.random() * 10));
  
  // Whoops added too many spaces
  greeting = greeting.trim();
  greeting += " ";
  
  let world = ["w", "o", "r", "l", "d"];
  
  greeting += world.reduce((flibbertigibbet, snollygoster) => flibbertigibbet + snollygoster)
  
  greeting += String.fromCharCode(33);
  return greeting;
}