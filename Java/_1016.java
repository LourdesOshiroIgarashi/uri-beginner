import java.util.Scanner;
import java.io.IOException;
public class _1016 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        int distancia, tempo;

        distancia = sc.nextInt();
        tempo = distancia * 2;
        
        System.out.printf("%d minutos\n", tempo);
    }

}
