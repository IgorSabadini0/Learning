print(f"-"*30)
print(f"D E T E C T O R   D E   P E S A D O")
print(f"_"*30)
maior = 0
for i in range (1, 6):
    nome = input(f"Digite o {i}º nome: ")
    peso = float(input(f"Digite o {i}º peso em KG: "))

    if peso > maior:
        maior = peso
        pesado = nome

print(f"Mais pesado: {pesado} com {maior} KG")