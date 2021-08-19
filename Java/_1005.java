import java.util.Scanner;
import java.io.IOException;
public class _1005 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        double nota1 =sc.nextDouble();
        double nota2 =sc.nextDouble();
        double peso1, peso2;
        peso1 = 3.5;
        peso2 = 7.5;
        
        double media = ((nota1 * peso1) + (peso2 * nota2)) / 11.0;
        
        System.out.printf("MEDIA = %.5f\n", media);
    }

}
