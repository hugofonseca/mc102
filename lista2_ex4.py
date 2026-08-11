ehPrimo = False

x = int(input("Digite um numero: "))

for i in range(x, 0, -1):
    if ehPrimo == False:
        dividendo = i
        for divisor in range(dividendo-1, 0, -1):
            if divisor != 1 and dividendo != divisor and dividendo % divisor == 0:
                break
            elif divisor == 1:
                ehPrimo = True
                break
    else:
        print(f"{dividendo} é o num primo mais próx ou igual a {x}")
        break        