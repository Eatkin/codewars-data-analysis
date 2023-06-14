# https://www.codewars.com/kata/5ac6932b2f317b96980000ca
# 2023-05-30T18:53:47.760+0000
function Get-MinValue ([int[]]$values)
{
  $values = $values | Sort-Object
  $seen = New-Object System.Collections.ArrayList
  $output = ""
  foreach ($value in $values)
  {
    if (-Not ($value -in $seen))
    {
      $output += [string]$value
      $seen += $value
    }
  }
  return $output
}