# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
# 2023-05-30T17:51:35.452+0000
function array_plus_array($arr1,$arr2){
  $length = $arr1.Length
  $sum = 0
  for ($i = 0; $i -lt $length; $i++)
  {
    $sum += $arr1[$i] + $arr2[$i]
  }
  return $sum
}