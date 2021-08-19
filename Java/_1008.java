import java.util.Scanner;
import java.io.IOException;
public class _1008 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        int identificacao = sc.nextInt();
        int horasTrabalhadas = sc.nextInt();
        double recebePorHora = sc.nextDouble();
        double salario;
        
        salario = horasTrabalhadas * recebePorHora;
        
        System.out.printf("NUMBER = %d\n", identificacao);
        System.out.printf("SALARY = U$ %.2f\n", salario);
    }

}
