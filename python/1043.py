a, b, c = map(float, input().split())

if a < b + c and b < a + c and c < a + b:
    perimetro = a + b + c
    print("Perimetro = {0:.1f}".format(perimetro))
else:
    area = (a + b) * c / 2
    print("Area = {0:.1f}".format(area))
