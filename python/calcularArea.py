from rich import print

while True:    
    print(f'\n[bold blue]------------ MENU ------------')
    print(f'\n[0] - [bold red]SAIR DO PROGRAMA')
    print(f'[1] - Quadrado')
    print(f'[2] - Retângulo')
    print(f'[3] - Triângulo')
    print(f'[4] - Círculo')
    op = int(input('\nEscolha uma figura para calcuar a área: '))

    match op:
        case 0:
            print(f'PROGRAMA ENCERRADO')
            break
        case 1:
            lado = float(input('Lado do Quadrado: '))
            if lado <= 0:
                print(f'\nDigite um valor [bold]MAIOR[/bold] que zero')
            else:
                area = lado ** 2
                print(f'A area do quadrado é {area:.2f}')
        case 2:
            base = float(input('Base do retângulo: '))
            altura = float(input('Altura do retângulo: '))
            if base <= 0 or altura <= 0:
                print(f'\nDigite um valor [bold]MAIOR[/bold] que zero')
            else:
                area = base * altura
                print(f'A área do retângulo é {area:.2f}')
        case 3:
            base = float(input('Base do triângulo: '))
            altura = float(input('Altura do triângulo: '))
            if base <= 0 or altura <= 0:
                print(f'\nDigite um valor [bold]MAIOR[/bold] que zero')
            else:
                area = (base * altura) / 2
                print(f'A área do triângulo é {area:.2f}')
        case 4:
            raio = float(input('Raio do círculo: '))
            if raio <= 0:
                print(f'\nDigite um valor [bold]MAIOR[/bold] que zero')
            else:
                area = 3.14 * raio**2
                print(f'A área do círculo é {area:.2f}')
        case _:
            print(f'\n [bold red]ERRO[/bold red] - Digite uma opção válida !')