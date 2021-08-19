import java.io.IOException;
import java.util.Scanner;

public class _1037
{
 
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        double x;
        x = sc.nextDouble();

        if (x <= 100 && x > 75)
        {
            System.out.printf("Intervalo (75, 100]\n");
        }
        else if (x <= 75 && x > 50)
        {
            System.out.printf("Intervalo (50, 75]\n");
        }
        else if (x <= 50 && x > 25)
        {
            System.out.printf("Intervalo (25, 50]\n");
        }
        else if (x <= 25 && x >= 0)
        {
            System.out.printf("Intervalo [0, 25]\n");
        }
        else
        {
            System.out.printf("Fora de intervalo\n");
        }
    }
 
}
