import time

saldo = 1000.00

def exibir_saldo():
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def sacar():
    global saldo
    global opcao
    valor = float(input("\nDigite o valor do saque: R$ "))
    if valor <= saldo:
        saldo = float(saldo - valor)
        print(f"Saque realizado com sucesso!")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    else:
        print(f"Saldo insuficiente para saque.")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

def depositar():
    global saldo
    valor = float(input("\nDigite o valor do deposito: R$ "))
    saldo = float(saldo + valor)
    print(f"Deposito realizado com sucesso!")
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")

while True:
    time.sleep(1)
    print(f"\n1 - Consultar saldo")
    print(f"2 - Saque")
    print(f"3 - Depositar")
    print(f"4 - Sair")
    opcao = int(input(f"\nDigite sua opção: "))

    match opcao:
        case 1: exibir_saldo()

        case 2: sacar()

        case 3: depositar()

        case 4:
            break
        
        case _:
            print(f"Opção inválida")