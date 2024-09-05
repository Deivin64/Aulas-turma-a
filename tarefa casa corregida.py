litros = float(input("quantos litros"))
tipo = input("qual o combustivel:")

if tipo == "G" or tipo == "g":
    valor = litros *5.8
    print(f"Olá vc abasteceu {litros} litros de gasolina\n"
          f"e gastou {valor}")
elif tipo == "E" or tipo == "e":
    valor = litros *4.9
    print(f"Olá vc abasteceu {litros} litros de etanol\n"
         f"e gastou {valor}")



