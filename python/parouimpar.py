def verificar(v: int):

    if v % 2 == 0:
        print(f"É Par")
    else:
        print(f"É Impar")

n = int(input(f"Informe o número: "))
verificar(n)