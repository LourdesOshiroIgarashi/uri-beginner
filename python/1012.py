a, b, c = map(float, input().split(" "))

tri = a * c / 2
cir = 3.14159 * (c ** 2)
tra = (a + b) * c / 2
qua = b * b
retan = a * b

print("TRIANGULO: {0:.3f}".format(tri))
print("CIRCULO: {0:.3f}".format(cir))
print("TRAPEZIO: {0:.3f}".format(tra))
print("QUADRADO: {0:.3f}".format(qua))
print("RETANGULO: {0:.3f}".format(retan))
