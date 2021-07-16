n1, n2, n3, n4 = map(int, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: {0:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {0:.1f}".format(exame))
    final = (media + exame) / 2
    if final >= 5:
        print("Aluno aprovado.")
        print("Media final: {0:.1f}".format(final))
    else:
        print("Aluno reprovado.")
        print("Media final: {0:.1f}".format(final))
