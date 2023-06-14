# https://www.codewars.com/kata/562f91ff6a8b77dfe900006e
# 2023-05-29T18:18:56.448+0000
function movie([int]$card, [int]$ticket, [double]$percent)
{
  $totalSpend = $card
  $ticketsBought = 0
  while ([Math]::Ceiling($totalSpend) -ge $ticketsBought * $ticket) 
  {
    $ticketsBought++
    $totalSpend += $ticket * [Math]::Pow($percent, $ticketsBought)
  }
  return $ticketsBought
}