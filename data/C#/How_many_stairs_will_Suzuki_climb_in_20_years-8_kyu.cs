// https://www.codewars.com/kata/56fc55cd1f5a93d68a001d4e
// 2023-05-19T13:14:22.462+0000
using System;
public class Kata
{
  public static long StairsIn20(int[][] stairs)
  {
    int total = 0;
    for (int i = 0; i < stairs.Length; i++)
      for (int j = 0; j < stairs[i].Length; j++)
        total += stairs[i][j];
    
    return total * 20;
  }
}