"""Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
Considerar que a média é ponderada e que o pesos das notas é 2, 3 e 5. Fórmula para o cálculo da média
final é: """

n1 = float(input(f'Digite a Nota 1: '))
n2 = float(input(f'Digite a Nota 2: '))
n3 = float(input(f'Digite a Nota 3: '))
pesos = [2, 3, 5]
pesos_soma = pesos[0] + pesos[1] + pesos[2] #tambem pode ser feito como: sum(pesos) que desse modo ja soma todos os itens do array.

mediaFinal = ((n1 * pesos[0]) + (n2 * pesos[1]) + (n3 * pesos[2])) / pesos_soma
print(f'Sua média final é {mediaFinal:.2f}')