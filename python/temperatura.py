"""Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius 
baseado na fórmula C = 5/9 * (F-32):""" 

fahrenheit = float(input('Digite o valor em Fº (Fahrenheit): '))

celsius = 5/9 * (fahrenheit-32)
print(f'O valor em Cº é de {celsius}')