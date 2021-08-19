import java.util.Scanner;
import java.io.IOException;

public class aumento_de_salario_1048 {
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        double salario, reajuste, novo, percentual;
        salario = sc.nextDouble();

        if (salario > 0 && salario < 400.00)
        {
            novo = salario + (salario * 0.15);
        }
        else if (salario < 800.00 && salario > 400.01)
        {
            novo = salario + (salario * 0.12);
        }
        else if (salario < 1200.00 && salario > 800.01)
        {
            novo = salario + (salario * 0.10);
        }
        else if (salario < 2000.00 && salario > 1200.01)
        {
            novo = salario + (salario * 0.07);
        }
        else
        {
            novo = salario + (salario * 0.04);
        }
        
        reajuste = novo - salario;
        percentual = (novo - salario) / salario * 100; 

        System.out.printf("Novo salario: %.2f\n", salario);
        System.out.printf("Reajuste ganho: %.2f\n", reajuste);
        System.out.printf("Em percentual: %d %\n", percentual);
    }
}
