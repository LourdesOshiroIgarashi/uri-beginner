import java.util.Scanner;
public class _1002 {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        double pi=3.14159;
        double raio;
        raio =sc.nextDouble();
        
        double area = pi * (raio*raio);
        
        System.out.printf("A=%.4f\n", area);
    }

}
