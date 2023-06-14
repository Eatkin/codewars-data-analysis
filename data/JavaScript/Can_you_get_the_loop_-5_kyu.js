// https://www.codewars.com/kata/52a89c2ea8ddc5547a000863
// 2023-06-01T15:18:01.779+0000
function loop_size(node){
  let slow = node;
  let fast = node;

  do {
    slow = slow.next;
    fast = fast.next.next;
  } while (slow !== fast);

  let count = 1;
  slow = slow.next;
  while (slow !== fast) {
    count++;
    slow = slow.next;
  }

  return count;
}