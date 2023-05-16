// https://www.codewars.com/kata/54edbc7200b811e956000556
// 2023-04-29T12:03:36.619+0000
#include <stdbool.h>
#include <stddef.h>

size_t count_sheep(const bool sheep[/* count */], size_t count)
{
  int num_sheep = 0;
  for (size_t i = 0; i < count; i++)
    if (sheep[i])
      num_sheep++;
      
  return num_sheep;
}