""" Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever:
- o maior preço lido
- a média aritmética dos preços dos produtos """

precos = []

for i in range (15):
    preco = float(input(f"O Preço do {i+1}º produto: "))
    codigo = input(f"Informe o código do {i+1}º produto: ")
    precos.append(preco)

media = sum(precos) / len(precos)
            maior_preco = max(precos)

print(f"O maior preço lido foi de {maior_preco} e a média aritmética dos preços dos produtos é de {media}")