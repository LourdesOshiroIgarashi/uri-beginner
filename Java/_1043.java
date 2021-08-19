/*
Só irá existir um triângulo se, somente se, 
os seus lados obedeceram à seguinte regra: 
um de seus lados deve ser maior que o valor absoluto (módulo) 
da diferença dos outros dois lados 
e menor que a soma dos outros dois lados. 

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
*/

import java.io.IOException;
import java.util.Scanner;
public class _1043 {
 
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        double a, b, c, area, perimetro, moda, modb, modc;
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();

        moda = 0;
        modb = 0;
        modc = 0;

        if ( a < b + c && (a > c - b || a > b - c))
        {
            moda = 1;
        }
        if ( b < a + c && (b > c - a || b > a - c))
        {
            modb = 1;
        } 
        if ( c < b + a && (c > a - b || c > b - a))
        {
            modc = 1;
        }

        if (moda == 1 && modb == 1 && modc == 1)
        {
            perimetro = a + b +c;
            System.out.printf("Perimetro = %.1f\n", perimetro);
        }
        else
        {
            area = (a + b) * c / 2;
            System.out.printf("Area = %.1f\n", area);
        }
 
    }
 
}
