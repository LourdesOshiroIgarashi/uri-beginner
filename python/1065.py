lista = []
par = 0

for i in range(5):
    lista.append(int(input()))

for i in lista:
    if  i % 2 == 0:
        par += 1
print("{} valores pares".format(par))
