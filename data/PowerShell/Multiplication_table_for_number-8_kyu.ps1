# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
# 2023-05-31T10:21:27.059+0000
function Multi-Table ([int] $n) {
  $output = ""
  for ($i = 1; $i -lt 10; $i++)
  {
    $product = $i * $n
    $output += "${i} * ${n} = ${product}`n"
  }
  # Add the last line
  $product = 10 * $n
  $output += "10 * ${n} = ${product}"
  return $output
}