import java.util.Scanner;
import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        int n, cont;
        n = sc.nextInt();

        for (int i = 2; i <= n; i += 2)
        {
            System.out.printf("%d^2 = %d\n", i, i * i);
        }
    }
}
