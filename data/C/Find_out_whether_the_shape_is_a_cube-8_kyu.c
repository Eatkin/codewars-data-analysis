// https://www.codewars.com/kata/58d248c7012397a81800005c
// 2023-05-19T07:16:57.159+0000
#include <stdbool.h>

bool cube_checker(int volume, int side) {
  if (side < 0 && volume < 0)
    return false;
  if (side == 0 && volume == 0)
    return false;
  
  int other_sides = volume / side;
  return other_sides == side * side;
}