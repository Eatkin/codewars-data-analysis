// https://www.codewars.com/kata/54147087d5c2ebe4f1000805
// 2023-05-19T07:06:49.567+0000
#include <stdbool.h>

void _if(bool value, void (*func1)(), void (*func2)())
{
  if (value)
    func1();
  else
    func2();
}