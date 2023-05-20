// https://www.codewars.com/kata/56530b444e831334c0000020
// 2023-05-19T08:31:08.310+0000
public class Kata
{
  public static string ChromosomeCheck(string sperm)
  {
    if (sperm == "XY")
      return "Congratulations! You're going to have a son.";
    if (sperm == "XX")
      return "Congratulations! You're going to have a daughter.";
    return "What";
  }
}