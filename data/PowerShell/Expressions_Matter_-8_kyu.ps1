# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
# 2023-05-31T10:08:14.973+0000
function ExpressionMatter([int] $a, [int] $b, [int] $c) {
  # Create an array of the values from every possible combo
  $values = ($a + $b + $c), ($a * $b * $c), (($a + $b) * $c), ($a * ($b + $c))
  return ($values | Measure-Object -Maximum).Maximum
}