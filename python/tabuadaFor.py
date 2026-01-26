n = int(input("Digite um número de 1 até 10: "))

if n > 10:
    print("Inválido. Insira um número de 1 a 10 !")
else:
    for i in range(0, 11):
        print(f"{i} x {n} = {i * n}")