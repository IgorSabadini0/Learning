"""As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
escreva o custo total da compra"""

macas_compradas = int(input('Quantas maças foram compradas: '))
preco_maca = float(1.3)
if macas_compradas >= 12:
    preco_maca = 1

preco_final = preco_maca * macas_compradas
sem_desconto = float(1.3 * macas_compradas)
economia = sem_desconto - preco_final

print(f'O preço final da compra é {preco_final:.2f}')

if economia > 0:
    print(f'Você teve uma economia de {economia:.2f}')
else:
    print(f'Compre 12 ou mais maçãs para obter um desconto')