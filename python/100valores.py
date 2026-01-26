"""Faça um programa que leia 100 valores e no final, escreva o maior e o menor valor lido. """

maior = 0
menor = 0

for i in range (1, 6):
    n = float(input(f"Digite o valor {i}: "))
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('-' * 30)
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')