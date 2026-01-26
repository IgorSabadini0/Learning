import random

x = random.randrange(101)
n = None
tentativas = 0

while n != x:
    n = int(input("Number: "))
    soma = 0
    tentativas = tentativas + 1
    if n == 101:
        print('Encerrando Joguinho')
        break
    elif n < x:
        print(f"More")
    elif n > x:
        print(f"Low")
    else:
        print(f"Congratulations")
        print(f"Tentativas: {tentativas - 1}")