from rich import print

a = input("Qual operação deseja realizar ? ('+, -, *, / ') ")

n1 = float(input("Qual o primeiro número ? "))
n2 = float(input("Qual o segundo número ? "))

if a == "+":
    print(f"[bold green]O resultado da soma é {n1 + n2} !")
elif a == "-":
    print(f"[bold green]O resultado da subtração é {n1 - n2} !")
elif a == "*":
    print(f"[bold green]O resultado da multiplicação é {n1 * n2} !")
elif a == "/":
    if n2 == 0:
        print(f"[bold red]Impossível dividir por zero ![/bold red]")
    else:
        print(f"[bold green]O resultado da divisão é {n1 / n2} !")
else:
                print("Operação inválida!")