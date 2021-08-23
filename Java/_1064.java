import java.util.Scanner;
import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        double x1, x2, x3, x4, x5, x6, media, soma;
        int contador, quantidade;
        contador = 1;
        media = 0.0;
        soma = 0.0;
        quantidade = 0;

        while (contador <= 6)
        {
            x1 = sc.nextDouble();
            if (x1 >= 0)
            {
                soma = soma + x1;
                quantidade += 1;
            }
            contador += 1;
        }
        media = soma / quantidade;

        System.out.printf("%d valores positivos\n", quantidade);
        System.out.printf("%.1f\n", media);
    }
}
