// https://www.codewars.com/kata/5715eaedb436cf5606000381
// 2023-05-03T14:16:10.209+0000
using System;
using System.Linq;

public class Kata
{
  public static int PositiveSum(int[] arr)
  {
    int sum = 0;
    foreach (int i in arr)
      sum += (i > 0) ? i : 0;
    return sum;
  }
}
