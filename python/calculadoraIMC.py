# CALCULADORA IMC
while True:
    peso = int(input("Peso (Kg): "))
    altura = float(input("Altura (Cm): ")) / 100
    calc = peso / (altura**2) 
    
    if calc < 18.5:
        print(f"\nBaixo Peso")
    elif calc >= 18.5 and calc < 24.99:
        print(f"\nNormal")
    elif calc >= 24.99 and calc <= 29.99:
        print(f"\nSobrepeso")
    elif calc > 30:
        print(f"\nObesidade")
    
    print(f"\nO valor do calculo é {calc}")