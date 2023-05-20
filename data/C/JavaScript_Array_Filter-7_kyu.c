// https://www.codewars.com/kata/514a6336889283a3d2000001
// 2023-05-19T07:05:27.853+0000
#include <stddef.h>

//  assign even numbers to preallocated *filtered
//  set pointer *f to length of this return array

void get_even_numbers(size_t a, const int array[a], int *filtered, size_t *f) {
  *f = 0;
  for (size_t i = 0; i < a; i++)
    if (array[i] % 2 == 0)  {
      filtered[*f] = array[i];
      (*f)++;
    }
}