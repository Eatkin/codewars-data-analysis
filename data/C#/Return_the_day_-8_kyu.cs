// https://www.codewars.com/kata/59dd3ccdded72fc78b000b25
// 2023-05-19T10:07:37.379+0000
using System.Collections;

public class Kata
{
  public static string WhatDay(int n)
  {
    Hashtable days = new Hashtable();
    days.Add(1, "Sunday");
    days.Add(2, "Monday");
    days.Add(3, "Tuesday");
    days.Add(4, "Wednesday");
    days.Add(5, "Thursday");
    days.Add(6, "Friday");
    days.Add(7, "Saturday");
    if (days.ContainsKey(n)) {
      return (string)days[n];
     }
    return "Wrong, please enter a number between 1 and 7";
  }
}