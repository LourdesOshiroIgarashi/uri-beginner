import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        int n, cont, num, quantidade, dentro, fora;
        n = sc.nextInt();
        cont = 0;
        dentro = 0;
        fora = 0;

        while (cont < n)
        {
            num = sc.nextInt();
            if (num >= 10 && num <= 20)
            {
                dentro += 1;
            }
            else
            {
                fora += 1;
            }
            cont += 1;
        }

        System.out.printf("%d in\n", dentro);
        System.out.printf("%d out\n", fora);
    }
}