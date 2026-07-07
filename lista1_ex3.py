#ler um valor e calcular f(x) = (sqrt(x)) + (x/2) + (x^x)
x = float(input("Entre com um numero ponto flutuante: "))
resultado = (x ** 0.5) + (x / 2) + (x ** x)
print("f(",x,") = ", resultado)