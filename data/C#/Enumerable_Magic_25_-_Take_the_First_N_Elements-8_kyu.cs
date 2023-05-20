// https://www.codewars.com/kata/545afd0761aa4c3055001386
// 2023-05-19T12:10:20.115+0000
using System;
using System.Linq;

public static class Kata
{
    public static int[] Take(int[] arr, int n)
    {
        return arr.Take(n).ToArray();
    }
}