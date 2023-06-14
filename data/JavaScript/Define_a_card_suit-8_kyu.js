// https://www.codewars.com/kata/5a360620f28b82a711000047
// 2023-06-02T09:29:46.879+0000
SUITS = {
  '♣': 'clubs',
  '♦': 'diamonds',
  '♥': 'hearts',
  '♠': 'spades'
}
function defineSuit(card) {
  return SUITS[card.slice(-1)];
}