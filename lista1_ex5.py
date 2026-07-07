#recebe os lados de um triangulo, classifica e calcula area na formula de heron
a = float(input("Entre com um valor: "))
b = float(input("Entre com um valor: "))
c = float(input("Entre com um valor: "))

if (a == b) and (b == c):
    print("Equilatero")
elif (a == b) or (a == c) or (b == c):
    print("Isosceles")
else:
    print("Escaleno")

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Area = ", area)