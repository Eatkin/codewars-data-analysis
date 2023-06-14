# https://www.codewars.com/kata/569218bc919ccba77000000b
# 2023-05-29T19:44:37.255+0000
function date-nb-days([int]$a0, [int]$a, [int]$p)
{
  $days = 0
  [double]$p = 1 + $p / 36000
  $a0 = [double]$a0
  while ($a0 * [Math]::Pow($p, $days) -le $a)
  {
    $days++
  }

  # Now we know how many days have passed we can start constructing the date
  $date = Get-Date -Year 2016 -Month 1 -Day 1
  $newDate = $date.AddDays($days)
  
  $formattedDate = $newDate.ToString("yyyy-MM-dd")
  return $formattedDate
}