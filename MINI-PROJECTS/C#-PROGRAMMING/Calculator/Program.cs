using System;
namespace Calculator
{
  class Program
  {
    static void Main(string[] args)
    {
      var firstNumber = 10;
      var secondNumber = 5;

      var sum = firstNumber + secondNumber;
      var difference = firstNumber - secondNumber;
      var multiplication = firstNumber * secondNumber;
      var division = firstNumber / secondNumber;
      var reminder = firstNumber % secondNumber;

      Console.WriteLine("Sum:" + sum);
      Console.WriteLine("Difference:" + difference);
      Console.WriteLine("Multiplication:" + multiplication);
      Console.WriteLine("Division:" + division);
      Console.WriteLine("Reminder:" + reminder);
    }
  }
}