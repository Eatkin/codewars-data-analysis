# https://www.codewars.com/kata/569b5cec755dd3534d00000f
# 2023-05-30T08:51:53.923+0000
function new-avg($arr, $navg)
{
   if ($arr.Length -eq 0)
   {
    return $navg
   }
   
   $sum = 0
   foreach ($item in $arr)
   {
    $sum += $item
   }
   
   $donationRequired = $navg * ($arr.Length + 1) - $sum
   if ($donationRequired -le 0)
   {
    return -1
   }
   return [Math]::Ceiling($donationRequired)
}