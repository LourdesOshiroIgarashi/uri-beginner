import java.util.Scanner;
import java.io.IOException;

public class _1048 {
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        double salario, reajuste, novo, percentual;
        salario = sc.nextDouble();

        if (salario >= 0 && salario <= 400.00)
        {
            percentual = 15;
        }
        else if (salario <= 800.00 && salario >= 400.01)
        {   
            percentual = 12;
        }
        else if (salario <= 1200.00 && salario >= 800.01)
        {
            percentual = 10;
        }
        else if (salario <= 2000.00 && salario >= 1200.01)
        {
            percentual = 7;
        }
        else
        {
            percentual = 4;
        }
        
        novo = salario + (salario * 0.01 * percentual);
        reajuste = novo - salario;

        System.out.printf("Novo salario: %.2f\n", novo);
        System.out.printf("Reajuste ganho: %.2f\n", reajuste);
        System.out.printf("Em percentual: %.0f %%\n", percentual);
    }
}
