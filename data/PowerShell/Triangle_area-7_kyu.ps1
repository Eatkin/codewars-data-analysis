# https://www.codewars.com/kata/59bd84b8a0640e7c49002398
# 2023-05-30T12:03:41.494+0000
function Triangle-Area([string]$triangle)
{
  $count = ($triangle | Select-String -Pattern '\n' -AllMatches).Matches.Count
  return [Math]::Pow($count - 2, 2) * 0.5
}