using System;
namespace _1002
{
    class _1002
    {
        static void Main(string[] args)
        {
            double pi = 3.14159;
            double raio = double.Parse(Console.ReadLine());
            double area = pi * raio * raio;


            Console.WriteLine("A="+ (area.ToString("F4")), area); // F para 2 casas após a virgula, C para valores monetarios (R$)
            //Console.WriteLine("A="+ Math.Round(area, 4));

            Console.ReadLine();
        }
    }
}
