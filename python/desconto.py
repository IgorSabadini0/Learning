valor = float(input('Qual o valor do produto ? '))

print(f'[1] Dinheiro ou PIX')
print(f'[2] Cartão de crédito 1x')
print(f'[3] Cartão de crédito 2x')
print(f'[4] Cartão de crédito 3x ou +')
pagamento = int(input('Qual a forma de pagamento ? '))

match pagamento:
    case 1:
        valor = valor - (valor*0.15)
    case 2:
        valor = valor - (valor*0.1)
    case 3:
        valor
    case 4:
        valor = valor + (valor*0.1)
    case _:
        print(f'INVÁLIDO')

print(f'O valor final do seu produto é de R$ {valor}')