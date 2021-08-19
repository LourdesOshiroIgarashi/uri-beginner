import java.util.Scanner;
import java.io.IOException;
public class _1014 {
    public static void main(String args[]) throws IOException{
        Scanner sc=new Scanner(System.in);
        int distancia;
        double combustivel, consumo;
        distancia = sc.nextInt();
        combustivel = sc.nextDouble();
        
        consumo = distancia / combustivel;
        
        System.out.printf("%.3f km/l\n", consumo);
    }

}
