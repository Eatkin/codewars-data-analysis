// https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e
// 2023-05-19T07:50:02.590+0000
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

int compare( const void* a, const void* b)
  {
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     // an easy expression for comparing
     return (int_a < int_b) - (int_a > int_b);
  }


int diffsum(const int* arr, size_t n)
{
    if (n < 2)
      return 0;
  
    qsort(arr, n, sizeof(int), compare);

    int sum = 0;

    for (size_t i = 0; i < n - 1; i++) {
        sum += arr[i] - arr[i + 1];
    }
  
    return sum;
}