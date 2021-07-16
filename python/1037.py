# Você deve fazer um programa que leia um valor qualquer
# e apresente uma mensagem dizendo em qual dos seguintes intervalos
# ([0,25], (25,50], (50,75], (75,100]) este valor se encontra.
# Obviamente se o valor não estiver em nenhum destes intervalos,
# deverá ser impressa a mensagem “Fora de intervalo” .

a = float(input())

if a >= 0 and a <= 25:
    print ("Intervalo [0, 25]")
elif a > 25 and a <= 50:
    print("Intervalo (25, 50]")
elif a > 50 and a <= 75:
    print("Intervalo (5, 75]")
elif a > 75 and a <= 100:
    print("Intervalo (75, 100]")
else:
    print("Fora de intervalo")
