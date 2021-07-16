codigo, quantidade = map(float, input().split(' '))

if codigo == 1:
    x = quantidade * 4.00
    print("Total: R$ {0:.2f}".format(x))

elif codigo == 2:
    x = quantidade * 4.50
    print("Total: R$ {0:.2f}".format(x))

elif codigo == 3:
    x = quantidade * 5.00
    print("Total: R$ {0:.2f}".format(x))

elif codigo == 4:
    x = quantidade * 2.00
    print("Total: R$ {0:.2f}".format(x))

elif codigo == 5:
    x = quantidade * 1.50
    print("Total: R$ {0:.2f}".format(x))

else:
    print("ta errado")
