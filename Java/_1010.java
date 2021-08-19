import java.util.Scanner;
import java.io.IOException;
public class _1010 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        int peca1, peca2, quantidade1, quantidade2;
        double precototal, preco1, preco2;

        peca1 = sc.nextInt();
        quantidade1 = sc.nextInt();
        preco1 = sc.nextDouble();
        
        peca2 = sc.nextInt();
        quantidade2 = sc.nextInt();
        preco2 = sc.nextDouble();
        
        precototal = (quantidade1 * preco1) + (quantidade2 * preco2);
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", precototal);
    }

}
