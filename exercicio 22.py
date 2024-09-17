nota1 = float(input("digite sua nota: "))
while nota1 < 0 or nota1 >10:
    nota1 = float(input("nota inválida\n"
                    "digite nota1 novamente"))
nota2 = float(input("nota do aluno: "))
while nota2 <0 or nota2>10:
    nota2 = float(input("Nota inválida\n]"
                        "Digite nota2 novamente: "))
    media = (nota1+nota2)/2
    print(media)