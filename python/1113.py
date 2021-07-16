x, y = map(int, input().split(" "))

while x != y:
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
    x, y = map(int, input().split(" "))
