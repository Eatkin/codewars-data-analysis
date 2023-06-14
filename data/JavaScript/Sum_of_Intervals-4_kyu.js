// https://www.codewars.com/kata/52b7ed099cdc285c300001cd
// 2023-06-02T14:57:32.750+0000
function sumIntervals(intervals) {
  let sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);
  let result = 0;
  let [start, end] = sortedIntervals[0];

  for (let i = 1; i < sortedIntervals.length; i++) {
    let [nextStart, nextEnd] = sortedIntervals[i];

    if (nextStart <= end) {
      end = Math.max(end, nextEnd);
    } else {
      result += end - start;
      start = nextStart;
      end = nextEnd;
    }
  }

  result += end - start;
  return result;
}