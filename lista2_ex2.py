qtd = int(input("Digite a qtd de numeros: "))
ok = True

for i in range(1, qtd+1):
    valor = int(input("Digite um valor: "))
    if i == 1:
        antecessor = valor
    else:
        if valor < antecessor:
            ok = False
        antecessor = valor

if ok == True:
    print("crescente")
else:
    print("não crescente")