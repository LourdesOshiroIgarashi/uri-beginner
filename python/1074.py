x = int(input())
lista = []

for i in range(x):
    y = int(input())
    if y == 0:
        print("NULL")
    else:
        if y % 2 == 0:
            if y > 0:
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")
        else:
            if y > 0:
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")
