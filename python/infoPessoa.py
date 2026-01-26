nome = input('Nome: ')
idade = int(input('Idade: '))
peso = float(input('Peso (Kg): '))

print(f'Nome: {nome}')

print(f'Idade: {idade}')

print(f'Peso: {peso}')

if idade >= 18:
    print(f'Você é maior de idade')
else:
    print(f'Você é menor de idade')