x = int(input())

num = [61, 71, 11, 21, 32, 19, 27, 31]
cidades = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']

if x in num:
    for i in range(len(num)):
        if num[i] == x:
            print(cidades[i])
else:
    print("DDD nao cadastrado")
