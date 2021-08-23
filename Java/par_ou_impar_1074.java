import java.util.Scanner;
import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        int n, x1, par, impar, positivo, negativo, contador;
        contador = 1;
        positivo = 0;
        negativo = 0;
        impar = 0;
        par = 0;
        
        n = sc.nextInt();
        while (contador <= n)
        {
            x1 = sc.nextInt();
            if (x1 == 0)
            {
                System.out.printf("NULL\n");
            }
            else if (x1 >= 0)
            {
                positivo = positivo + 1;
                if (x1 % 2 == 0)
                {
                    par = par + 1;
                    System.out.printf("EVEN POSITIVE\n");
                }
                else
                {
                    impar = impar + 1;
                    System.out.printf("ODD POSITIVE\n");
                }
            }
            else
            {
                negativo = negativo + 1;
                if (x1 % 2 == 0)
                {
                    par = par + 1;
                    System.out.printf("EVEN NEGATIVE\n");
                }
                else
                {
                    impar = impar + 1;
                    System.out.printf("ODD NEGATIVE\n");
                }
            }
            contador += 1;
        }
    }
}