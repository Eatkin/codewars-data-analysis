// https://www.codewars.com/kata/57e921d8b36340f1fd000059
// 2023-05-19T08:39:51.796+0000
public class Kata
{
    public static string Shark(
      int pontoonDistance, 
      int sharkDistance, 
      int youSpeed, 
      int sharkSpeed, 
      bool dolphin)
    {
      if (dolphin)
        sharkSpeed /= 2;
      
      float timeUntilEaten = sharkDistance / sharkSpeed;
      float timeUntilSafe = pontoonDistance / youSpeed;
      
      return (timeUntilEaten > timeUntilSafe) ? "Alive!" : "Shark Bait!";
    }
}