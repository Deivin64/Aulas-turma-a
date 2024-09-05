nota1 =float(input("digite nota 1:"))
nota2 =float(input("digite nota 2:"))
nota3 =float(input("digite nota 3:"))
media =nota1+nota2+nota3/3
if media>=7:
    print("aprovado")
else:
    if media>=4:
        print("recuperacao")
    else:
        print("reprovado")
