op = 0
ok = True

while ok:
    print("1 - Pizza Marguerita")
    print("2 - Pizza de Calabresa")
    print("3 - Pizza de Pepperoni")
    print("4 - Pizza de Mussarela")
    print("5 - SAIR")

    op = input("Entre com o nº das opções acima: ")

    if op != "5":
        print(" Opção escolhida:", op)
    else:
        ok = False