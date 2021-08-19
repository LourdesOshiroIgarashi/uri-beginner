import java.io.IOException;
import java.util.Scanner;

public class _1042 
{
 
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        int a, b, c, maior, menor, meio;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        maior = a;
        meio = b;
        menor = c;

        if (a <= b && a <= c)
        {
            menor = a;
            if (b <= c)
            {
                maior = c;
                meio = b;
            }
            else
            {
                meio = c;
                maior = b;
            }
        }
        else if (b <= a && b <= c)
        {
            menor = b;
            if (a <= c)
            {
                maior = c;
                meio = a;
            }
            else
            {
                meio = c;
                maior = a;
            }
        }
        else if (c <= b && c <= a)
        {
            menor = c;
            if (b <= a)
            {
                maior = a;
                meio = b;
            }
            else
            {
                meio = a;
                maior = b;
            }
        }
        
        System.out.printf("%d\n", menor);
        System.out.printf("%d\n", meio);
        System.out.printf("%d\n\n", maior);
        
        System.out.printf("%d\n", a);
        System.out.printf("%d\n", b);
        System.out.printf("%d\n\n", c);
    }
 
}
