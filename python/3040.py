n = int(input())

while n != 0:
    h, d, g = map(int, input().split(" "))
    if 200 <= h <= 300:
        if d >= 50:
            if g >= 150:
                print("Sim")

            else:
                print("Nao")

        else:
            print("Nao")

    else:
        print("Nao")

    n = n -1
