codigo1, x1, valor1 = map(float, input())
codigo2, x2, valor2 = map(float, input())

calculo1 = x1 * valor1
calculo2 = x2 * valor2

final = calculo1 + calculo2

print("VALOR A PAGAR: R$ {0:.2f}".format(final))
