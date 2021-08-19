n = int(input())

x = 0
y = 0
caso = 0


while n > 0:
    x, y = input().split(" ")
    n = n - 1
    caso = caso + 1

    if x == "tesoura" and y != "tesoura":
        if y == "papel" or y == "lagarto":
            print("Caso #{}: Bazinga!".format(caso))

        elif y == "pedra" or y == "Spock":
            print("Caso #{}: Raj trapaceou!".format(caso))

    elif x == "papel" and y != "papel":
        if y == "pedra" or y == "Spock":
            print("Caso #{}: Bazinga!".format(caso))

        elif y == "tesoura" or y == "lagarto":
            print("Caso #{}: Raj trapaceou!".format(caso))

    elif x == "lagarto" and y != "lagarto":
        if y == "papel" or y == "Spock":
            print("Caso #{}: Bazinga!".format(caso))

        elif y == "tesoura" or y == "pedra":
            print("Caso #{}: Raj trapaceou!".format(caso))

    elif x == "pedra" and y != "pedra":
        if y == "lagarto" or y == "tesoura":
            print("Caso #{}: Bazinga!".format(caso))

        elif y == "Spock" or y == "papel":
            print("Caso #{}: Raj trapaceou!".format(caso))

    elif x == "Spock" and y != "Spock":
        if y == "tesoura" or y == "pedra":
            print("Caso #{}: Bazinga!".format(caso))

        elif y == "papel" or y == "lagarto":
            print("Caso #{}: Raj trapaceou!".format(caso))

    else:
        print("Caso #{}: De novo!".format(caso))
