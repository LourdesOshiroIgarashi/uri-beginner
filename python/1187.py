operacao = input()
matriz = []
soma = 0
media = 0
inicial = 1
final = 10
total = 30

for i in range(12):
    x = []
    for j in range(12):
        x.append(float(input()))
    matriz.append(x)

for i in range(11):
    for j in range(inicial, final + 1):
        if operacao == "S":
            soma += matriz[i][j]
        elif operacao == "M":
            media += matriz[i][j]
    inicial += 1
    final -= 1
media = media / total

if operacao == "S":
    print("{0:.1f}".format(soma))
elif operacao == "M":
    print("{0:.1f}".format(media))
