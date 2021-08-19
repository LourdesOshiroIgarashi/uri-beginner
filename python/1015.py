import math

x1, y1 = map(float, input().split(" "))
x2, y2 = map(float, input().split(" "))

calculo = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
distancia = math.sqrt(calculo)
print("{0:.4f}".format(distancia))
