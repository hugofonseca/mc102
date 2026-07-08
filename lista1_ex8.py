ano = int(input("Entre com um ano: "))

if(ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0):
    print("Eh bissexto")
else:
    print("Nao eh bissexto")