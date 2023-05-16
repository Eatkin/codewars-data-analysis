// https://www.codewars.com/kata/57a429e253ba3381850000fb
2023-03-12T08:29:23.016+0000
function bmi(weight, height) {
  let bmi = weight / height ** 2;
  if (bmi <= 18.5)
    return "Underweight";
  if (bmi <= 25)
    return "Normal";
  if (bmi <= 30)
    return "Overweight"
  
  return "Obese"
}