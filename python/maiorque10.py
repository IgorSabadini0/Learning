"""Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10! """

valor = float(input('Digite um valor para verificar se é maior que 10: '))

if valor < 10:
    print(f'É MAIOR QUE 10!')
else:
    print(f'NÃO É MAIOR QUE 10!')