// https://www.codewars.com/kata/55cbd4ba903825f7970000f5
// 2023-05-18T09:26:15.717+0000
const Grades = {
  "A": 90,
  "B": 80,
  "C": 70,
  "D": 60,
  "F": 0
};

function getGrade (s1, s2, s3) {
  let avg_grade = (s1 + s2 + s3) / 3;
  for (let [grade, boundary] of Object.entries(Grades))
    if (avg_grade >= boundary)
      return grade;
}