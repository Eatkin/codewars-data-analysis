# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
# 2023-05-31T10:13:16.872+0000
function Get-CenturyFromYear ([int]$year)
{
  return [Math]::Floor(($year - 1) / 100) + 1
}