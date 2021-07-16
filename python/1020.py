idade = int(input())  # em dias

# ano = 365 dias
# mes = 30 dias

anos = idade // 365
mes = idade % 365 // 30
dias = (idade % 365) % 30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dias))
