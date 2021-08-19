import java.util.Scanner;
import java.io.IOException;

public class e_1038 
{
 
    public static void main(String[] args) throws IOException 
    {
        Scanner sc = new Scanner(System.in);
        int codigo;
        double total = 0;
        codigo = sc.nextInt();
        double quantidade = sc.nextDouble();

        if (codigo == 1)
        {
            total = quantidade * 4.0;
        }
        else if (codigo == 2)
        {
            total = quantidade * 4.5;
        }
        else if (codigo == 3)
        {
            total = quantidade * 5.0;
        }
        else if (codigo == 4)
        {
            total = quantidade * 2.0;
        }
        else if (codigo == 5)
        {
            total = quantidade * 1.5;
        }
        System.out.printf("Total: R$ %.2f\n", total);
    }
 
}
