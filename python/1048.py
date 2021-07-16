# Salário	Percentual de Reajuste
# 0 - 400.00   15
# 400.01 - 800.00   12
# 800.01 - 1200.00   10
# 1200.01 - 2000.00  7
# Acima de 2000.00   4

x = float(input())

if x <= 400:
    percentual = 0.15

elif 400.01 <= x <= 800:
    percentual = 0.12

elif 800.01 <= x <= 1200:
    percentual = 0.10

elif 1200.01 <= x <= 2000:
    percentual = 0.07

else:
    percentual = 0.04

novo = percentual * x + x
percentual = int(percentual * 100)
reajuste = novo - x
print("Novo salario: {0:.2f}".format(novo))
print("Reajuste ganho: {0:.2f}".format(reajuste))
print("Em percentual: {0:.0f} %".format(percentual))
