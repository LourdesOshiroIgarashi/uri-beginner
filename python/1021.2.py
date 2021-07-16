valor = float(input())

a = valor // 100  # 100
b = (valor % 100) // 50  # 50
c = ((valor % 100) % 50) // 20  # 20
d = (((valor % 100) % 50) % 20) // 10  # 10
e = (((valor % 100) % 50) % 20) % 10 // 5  # 5
f = ((((valor % 100) % 50) % 20) % 10) % 5 // 2  # 2
g = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 // 1  # 1
h = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 % 1 // 0.5  # 0.50
i = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 % 1 % 0.5 // 0.25  # 0.25
j = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 % 1 % 0.5 % 0.25 // 0.1  # 0.10
k = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 % 1 % 0.5 % 0.25 % 0.1 // 0.05  # 0.05
L = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 % 1 % 0.5 % 0.25 % 0.1 % 0.05 // 0.01  # 0.01

print("NOTAS:")
print("{0:.0f} nota(s) de R$ 100.00".format(a))
print("{0:.0f} nota(s) de R$ 50.00".format(b))
print("{0:.0f} nota(s) de R$ 20.00".format(c))
print("{0:.0f} nota(s) de R$ 10.00".format(d))
print("{0:.0f} nota(s) de R$ 5.00".format(e))
print("{0:.0f} nota(s) de R$ 2.00".format(f))
print("MOEDAS:")
print("{0:.0f} moeda(s) de R$ 1.00".format(g))
print("{0:.0f} moeda(s) de R$ 0.50".format(h))
print("{0:.0f} moeda(s) de R$ 0.25".format(i))
print("{0:.0f} moeda(s) de R$ 0.10".format(j))
print("{0:.0f} moeda(s) de R$ 0.05".format(k))
print("{0:.0f} moeda(s) de R$ 0.01".format(L))
