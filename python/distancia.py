# 22 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.
# Fórmula: distância = tempo x velocidade.
# litros usados = distância / 12.

velocidade = float(input('Velocidade: '))
tempo = float(input('Tempo (em HR): '))
distancia = tempo * velocidade

litros_usados = distancia / 12

print(f'a quantidade de litros utilizados para fazer a viagem é de {litros_usados:.2f}')
print(f'A velocidade média é de Km/h {velocidade}')
print(f'A distancia percorrida é de {distancia}')