pin = 1234
senha = int(input("informe sua senha: "))
tent = 1
while senha != pin and tent<3:
    senha = int(input(f"Senha errada\n"
                      f"voce tem {3-tent}\n"
                      f"informe sua senha novamente"))
    tent+=1
    if tent == 3 and senha != pin:
        print("senha bloqueada! chorou papai")
    else:
        print("Login efetuado com sucesso")