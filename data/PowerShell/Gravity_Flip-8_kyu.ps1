# https://www.codewars.com/kata/5f70c883e10f9e0001c89673
# 2023-05-30T19:13:51.823+0000
function flip([char] $dir, [int[]] $arr) {
  $arr = $arr | Sort-Object
  if ($dir -eq 'R')
  {
    return $arr
  }
  $reversed = $arr.Clone()
  [array]::Reverse($reversed)
  return $reversed
}