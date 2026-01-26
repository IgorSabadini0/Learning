""" A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado."""

km_percorrido = float(input(f"Quantidade de Km percorridos: "))
dias_alugado = int(input(f"Quantidade de dias alugados: "))
VALOR_DIA = 90
VALOR_KM = 0.2
preco_dias = dias_alugado * VALOR_DIA
preco_km = km_percorrido * VALOR_KM
preco_final = preco_dias + preco_km

print(f"\nAluguel de carro")
print(f"-" * 30)
print(f"- {dias_alugado} dias: R${preco_dias:.2f}")
print(f"- {km_percorrido} Km: R${preco_km:.2f}")
print(f"O total a pagar é: R${preco_final:.2f}")