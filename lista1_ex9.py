genero = str(input("Entre com F para feminino ou M para masculino: "))
idade = int(input("Entre com a idade: "))
tempoContrib = int(input("Entre com a qtd anos de contribuicao: "))

if (genero == "M"):
    if (idade >= 65) and (tempoContrib >= 10):
        print("Aposentavel")
    elif (idade >= 63) and (tempoContrib >= 15):
        print("Aposentavel")
    else:
        print("Nao eh aposentavel")
elif (genero == "F"):
    if (idade >= 63) and (tempoContrib >= 10):
        print("Aposentavel")
    elif (idade >= 61) and (tempoContrib >= 15):
        print("Aposentavel")
    else:
        print("Nao eh aposentavel")
else:
    print("Entrada invalida! Tente novamente")