// https://www.codewars.com/kata/57356c55867b9b7a60000bd7
// 2023-03-31T09:01:12.001+0000
#include <stdio.h>

int basic_op(char op, int value1, int value2) {
  if (op == '+')
      return value1 + value2;
  if (op == '-')
      return value1 - value2;
  if (op == '*')
      return value1 * value2;
  if (op == '/')  {
      if (value2 == 0)  {
        printf("Cannot divide by zero");
        return 0;
      }
      return value1 / value2;
  }
  printf("Invalid operator provided");
  return 0;
}