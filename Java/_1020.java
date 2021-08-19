import java.util.Scanner;
import java.io.IOException;
public class _1020 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        int entrada, dias, anos, meses;

        entrada = sc.nextInt();
        anos = entrada / 365;
        entrada = entrada - anos * 365;

        meses = entrada / 30;
        entrada = entrada - meses * 30;

        dias = entrada;

        System.out.printf("%d ano(s)\n", anos);
        System.out.printf("%d mes(es)\n", meses);
        System.out.printf("%d dia(s)\n", dias);
    }

}
