novo = 1
while novo == 1:

  x1 = float(input())
  while x1 > 10 or x1 < 0:
    print('nota invalida')
    x1 = float(input())

  x2 = float(input())
  while x2 > 10 or x2 < 0:
    print('nota invalida')
    x2 = float(input())

  media = (x1 + x2) / 2
  print('media = {0:.2f}'.format(media))

  print('novo calculo (1-sim 2-nao)')
  novo = int(input())
  while novo != 1 and novo != 2:
    print('novo calculo (1-sim 2-nao)')
    novo = int(input())
