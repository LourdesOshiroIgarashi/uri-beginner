n = int(input())
anoes = 0
elfos = 0
humanos = 0
magos = 0
hobbits = 0

while n > 0:
    nome, raça = map(str, input().split(" "))
    n = n - 1

    if raça == "A":
        anoes = anoes + 1

    elif raça == "E":
        elfos = elfos + 1

    elif raça == "H":
        humanos = humanos + 1

    elif raça == "M":
        magos = magos + 1

    else:
        hobbits = hobbits + 1

print("{} Hobbit(s)".format(hobbits))
print("{} Humano(s)".format(humanos))
print("{} Elfo(s)".format(elfos))
print("{} Anao(s)".format(anoes))
print("{} Mago(s)".format(magos))
