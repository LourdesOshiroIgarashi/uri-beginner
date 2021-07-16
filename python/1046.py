a, b = map(int, input().split())

if a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    if a > 12:
        x = 24 - a
        if b > 12:
            y = 24 - b
            total = x + y
            print("O JOGO DUROU {} HORA(S)".format(total))
        else:
            total = x + b
            print("O JOGO DUROU {} HORA(S)".format(total))
    else:
        if b > 12:
            total = b - a
            print("O JOGO DUROU {} HORA(S)".format(total))
        else:
            if a == 0 and b ==0:
                print("O JOGO DUROU 24 HORA(S)")
            else:
                if b > a:
                    total = b - a
                    print("O JOGO DUROU {} HORA(S)".format(total))
                else:
                    total = 24 - a
                    print("O JOGO DUROU {} HORA(S)".format(total))
