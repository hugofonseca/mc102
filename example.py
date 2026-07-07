print("Digite um número:")
a = int(input())
if (a % 2) == 0 and (a < 100):
    print("O número é par e menor do que 100")
elif (a % 2 == 0) and (a >= 100):
    print("O número é par e maior ou igual que 100")
elif (a % 2 != 0) and (a < 100):
    print("O número é ímpar e menor do que 100")
else:
#elif a % 2 != 0 and a >= 100:
    print("O número é ímpar e maior ou igual que 100")