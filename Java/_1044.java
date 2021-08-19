import java.util.Scanner;
import java.io.IOException;

public class _1044 {
    public static void main(String[] args) throws IOException 
    {
        Scanner sc = new Scanner(System.in);
        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();

        if (a % b == 0 || b % a == 0)
        {
            System.out.printf("Sao Multiplos");
        }
        else
        {
            System.out.printf("Nao sao Multiplos");
        }
    }
}
