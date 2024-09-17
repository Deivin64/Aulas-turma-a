quantalu =int(input("quantidade de alunos: "))
soma = 0
for x in range(quantalu):
    notas = float(input("digite uma nota: "))
    soma = soma + quantalu
media = notas / quantalu
print(media)
