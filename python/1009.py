nome = input()
fixo = float(input())
vendas = float(input())

bonus = vendas * 0.15
salario = bonus + fixo

print("TOTAL = R$ {0:.2f}".format(salario))
