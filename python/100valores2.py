valores = []

for i in range (1,6):
    n = float(input(f'Digite o {i}º valor: '))
    valores.append(n)

print(f"O maior valor é {max(valores)}")
print(f"O menor valor é {min(valores)}")