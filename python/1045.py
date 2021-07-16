a, b, c = map(float, input().split())

if b < c:
    aux = b
    b = c
    c = aux

if a < b:
    aux = a
    a = b
    b = aux

if a >= (b + c):
    print("NAO FORMA TRIANGULO")

else:
    if a * a == b * b + c * c:
        print("TRIANGULO RETANGULO")

    if a * a > b * b + c * c:
        print("TRIANGULO OBTUSANGULO")

    if a * a < b * b + c * c:
        print("TRIANGULO ACUTANGULO")

    if a == b and a == c:
        print("TRIANGULO EQUILATERO")

    if a == b or b == c or a == c:
        if a == b and b != c:
            print("TRIANGULO ISOSCELES")
        if a == c and a != b:
            print("TRIANGULO ISOSCELES")
        if b == c and a != b:
            print("TRIANGULO ISOSCELES")
