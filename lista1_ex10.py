x = float(input("Entre com um numero: "))
y = float(input("Entre com outro numero: "))
op = input("Entre a operacao +, -, *, /: ")

if (op == "+") or (op == "-") or (op == "*") or (op == "/"):
    if (op == "+"):
        print("soma = ", x + y)
    elif (op == "-"):
        print("subtracao = ", x - y)
    elif (op == "*"):
        print("produto = ", x * y)
    elif (op == "/"):
        print("divisao = ", x / y)
else:
    print("Entrada invalida! Tente novamente")