n = int(input())

x = n
y = 1

while n > 1:
    y = x * y
    n = n - 1
    x = x - 1

print(y)
