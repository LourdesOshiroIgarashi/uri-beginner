lista = []
positivo = 0

for i in range(6):
    lista.append(int(input()))

for i in lista:
    if i >= 0:
        positivo += 1

print("{} valores positivos".format(positivo))
