x = int(input())

a = 1
b = a ** 2
c = b * a

while x > 0:
    print(a, b, c)
    x = x - 1
    a = a + 1
    b = a ** 2
    c = b * a
