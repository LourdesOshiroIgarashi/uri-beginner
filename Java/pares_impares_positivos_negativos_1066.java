import java.util.Scanner;
import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        int x1, par, impar, positivo, negativo, contador;
        contador = 1;
        positivo = 0;
        negativo = 0;
        impar = 0;
        par = 0;

        while (contador <= 5)
        {
            x1 = sc.nextInt();
            if (x1 > 0)
            {
                positivo = positivo + 1;
                if (x1 % 2 == 0)
                {
                    par = par + 1;
                }
                else
                {
                    impar = impar + 1;
                }
            }
            else if (x1 == 0)
            {
                par = par + 1;
            }
            else 
            {
                negativo = negativo + 1;
                if (x1 % 2 == 0)
                {
                    par = par + 1;
                }
                else
                {
                    impar = impar + 1;
                }
            }
            contador += 1;
        }

        System.out.printf("%d valor(es) par(es)\n", par);
        System.out.printf("%d valor(es) impar(es)\n", impar);
        System.out.printf("%d valor(es) positivo(s)\n", positivo);
        System.out.printf("%d valor(es) negativo(s)\n", negativo);
    }
}