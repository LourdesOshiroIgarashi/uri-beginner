x = int(input())

while x != 0:
    matriz = []
    contadori = 1
    linha = 1
    soma = 0

    for i in range(x):
        linha = []
        for j in range(x):
            while linha < x:
                if i == 0 or i == x - 1 or j == 0 or j == x - 1:
                    linha.append(contadori)
                else:
                    if i == linha and j
                contadori += 1
                linha += 1
                soma += 1
        matriz.append(linha)