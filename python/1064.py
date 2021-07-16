lista = []
pos = 0
x = 0

for i in range(6):
    lista.append(float(input()))

for i in lista:
    if i >= 0:
        pos += 1
        x = i + x
media = x / pos
media = round(media)

print("{} valores positivos".format(pos))
print(media)
