op = str(input("Entre com C para Celsius ou F para Farenheit: "))
x = float(input("Entre com uma temperatura na unidade informada: "))

if (op != "C") and (op != "F"):
    print("Entrada invalida")
else:
    if (op == "C"):
        res = (x / 5 / 9) + 32
    else:
        res = (x - 32) * 5 / 9
    print("conversao = ", res)