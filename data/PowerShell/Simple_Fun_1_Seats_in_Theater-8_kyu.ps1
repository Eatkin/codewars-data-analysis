# https://www.codewars.com/kata/588417e576933b0ec9000045
# 2023-05-30T13:21:35.230+0000
function seats_in_theater {
    [OutputType([int])]
    Param ([int]$total_col, [int]$total_row, [int]$col, [int]$row)
    
    return ($total_col - $col + 1) * ($total_row - $row)
}