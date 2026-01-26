"""A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos
para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:

    a) Média de salário da população
    b) Média do número de filhos
    c) Maior salário dos habitantes
    d) Percentual de pessoas com salário menor que R$ 150,00

Obs.: O final da leituras dos dados se dará com a entrada de um “salário negativo”."""

salarios = []
filhos = []
populacao = 0
pessoa_salario_menor = 0


while True:
    salario = float(input(f"Informe seu salário: "))

    if salario < 0:
        break

    num_filhos = int(input(f"Informe o número de filhos: "))
    print(f"-" * 30)
    print(f"")
    
    if salario >= 0 and num_filhos >= 0:
        filhos.append(num_filhos)
        salarios.append(salario)
        populacao += 1
    else:
        print(f"Valores NEGATIVOS em filhos são computados como ZERO.")
        salarios.append(salario)
        num_filhos = 0
        filhos.append(num_filhos)
        populacao += 1

    if salario >= 0 and salario < 150:
        pessoa_salario_menor += 1

if len(salarios) > 0:
    media_salario = sum(salarios) / len(salarios)
    media_filhos = sum(filhos) / populacao
    maior_salario = max(salarios)
    percentual_salario_menor = (pessoa_salario_menor / populacao) * 100

    print(f"-" * 30)
    print(f'população: {populacao}')
    print(f'media de salario = R$ {media_salario:.2f}')
    print(f'media do numero de filhos = {media_filhos:.2f}')
    print(f'maior salario = R$ {maior_salario:.2f}')
    print(f'percentual de pessoas com salario menor que R$ 150,00 = {percentual_salario_menor:.2f}%')
else:
    print(f"\nNenhum dado foi coletado.")