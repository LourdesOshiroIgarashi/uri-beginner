linha = int(input())
operacao = input()
matriz = []
soma = 0
media = 0

for i in range(12):
    x = []
    for j in range(12):
        x.append(float(input()))
    matriz.append(x)

for j in range(12):
    if operacao == "S":
        soma += matriz[linha][j]
    elif operacao == "M":
        media += matriz[linha][j]
media = media / 12

if operacao == "S":
    print("{0:.1f}".format(soma))
elif operacao == "M":
    print("{0:.1f}".format(media))
