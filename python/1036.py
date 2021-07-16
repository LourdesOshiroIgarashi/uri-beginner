import math

a, b, c = map(float, input().split(" "))

delta = b*b - 4 * a * c

if a > 0 and delta > 0:
    if delta == 0:
        # raíz dupla
        x1 = (- b + math.sqrt(delta))/(2*a)
        print("R1 = {0:.5f}".format(x1))
        print("R2 = {0:.5f}".format(x1))
    else:
        # 2 raízes reais distintas
        x1 = (- b + math.sqrt(delta))/(2*a)
        x2 = (- b - math.sqrt(delta))/(2*a)
        print("R1 = {0:.5f}".format(x1))
        print("R2 = {0:.5f}".format(x2))
else:
    print("Impossivel calcular")
