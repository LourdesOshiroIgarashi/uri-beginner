x = int(input())
y = int(input())
soma = 0

if x > y:
    aux = x
    x = y
    y = aux

while x <= y:
    if x % 13 != 0:
        soma += x
        x += 1
    else:
        x += 1

print(soma)
