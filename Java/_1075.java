import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        int n, num;
        n = sc.nextInt();

        for (int i = 1; i <= 10000; i++)
        {
            if (i % n == 2)
            {
                System.out.printf("%d\n", i);
            }
        }
    }
}
