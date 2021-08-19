n = int(input())
lista = list(map(int, input().split()))
menor = lista[0]
posicao = 0

for i in range(len(lista)):
    if menor > lista[i]:
        menor = lista[i]
        posicao = i


print("Menor valor: {}".format(menor))
print("Posicao: {}".format(posicao))
