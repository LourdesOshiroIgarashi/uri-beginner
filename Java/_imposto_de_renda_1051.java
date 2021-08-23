import java.util.Scanner;
import java.io.IOException;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        double renda, imposto, total;
        renda = sc.nextDouble();
        total = 0;

        if (renda <= 2000 && renda >= 0)
        {
            System.out.printf("Isento\n");
        }
        else
        {
            if (renda <= 3000 && renda >= 2000.01)
            {
                renda -= 2000;
                total = renda * 0.08f;
            }
            else if (renda <= 4500 && renda >= 3000.01)
            {
                renda -= 3000;
                total += 80;
                total += renda *0.18f;
            }
            else
            {
                renda -= 4500;
                total += 350;
                total += renda *0.28f;
            }
            
            System.out.printf("R$ %.2f\n", total);
        }
        
    }
}