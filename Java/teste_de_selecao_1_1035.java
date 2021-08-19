import java.util.Scanner;
import java.io.IOException;
public class teste_de_selecao_1_1035 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        int a, b, c, d;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        
        if (b > c && d > a && c + d > a + b && c > 0 && d > 0)
        {
            System.out.printf("Valores aceitos");
        }
        else
        {
            System.out.printf("Valores nao aceitos");
        }
        
    }

}