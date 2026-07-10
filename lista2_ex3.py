m = int(input("Digite um numero: "))
n = int(input("Digite outro numero: "))
print("O MDC entre", m ,"e", n, "é")
while n != 0:
    resto = m % n
    m = n
    n = resto
print(m)