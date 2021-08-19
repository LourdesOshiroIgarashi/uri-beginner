def maior(x, y, z):
    if x >= y and x >= z:
        return print("{} eh o maior".format(x))
    elif y >= z and y >= x:
        return print("{} eh o maior".format(y))
    else:
        return print("{} eh o maior".format(z))


a, b, c = map(int, input().split(" "))
maior(a, b, c)
