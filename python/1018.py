valor = int(input())

a = valor // 100  # 100
b = (valor % 100) // 50  # 50
c = ((valor % 100) % 50) // 20  # 20
d = (((valor % 100) % 50) % 20) // 10  # 10
e = (((valor % 100) % 50) % 20) % 10 // 5  # 5
f = ((((valor % 100) % 50) % 20) % 10) % 5 // 2  # 2
g = (((((valor % 100) % 50) % 20) % 10) % 5) % 2 // 1  # 1

print(valor)
print("{} nota(s) de R$ 100,00".format(a))
print("{} nota(s) de R$ 50,00".format(b))
print("{} nota(s) de R$ 20,00".format(c))
print("{} nota(s) de R$ 10,00".format(d))
print("{} nota(s) de R$ 5,00".format(e))
print("{} nota(s) de R$ 2,00".format(f))
print("{} nota(s) de R$ 1,00".format(g))
