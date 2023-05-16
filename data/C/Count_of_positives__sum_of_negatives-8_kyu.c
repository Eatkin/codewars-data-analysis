// https://www.codewars.com/kata/576bb71bbbcf0951d5000044
// 2023-03-31T13:29:12.165+0000
#include <stddef.h>
#include <stdlib.h>

int* count_positives_sum_negatives(
  int *values, size_t count, int *positivesCount, int *negativesSum) 
{
  int posCount = 0;
  int negSum = 0;
  
  for (size_t i = 0; i < count; i++)  {
    if (values[i] > 0)
      posCount++;
    else if (values[i] < 0)
      negSum += values[i];
  }
  
  *positivesCount = posCount;
  *negativesSum = negSum;
  
  int *result = malloc(sizeof(int) * 2);
  result[0] = posCount;
  result[1] = negSum;
  return result;
}  