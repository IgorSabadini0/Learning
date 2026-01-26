"""Escreva um algoritmo que imprima as seguintes seqüências de números: (1, 1 2 3 4 5 6 7 8 9 10)
(2, 1 2 3 4 5 6 7 8 9 10) (3, 1 2 3 4 5 6 7 8 9 10) (4, 1 2 3 4 5 6 7 8 9 10) e assim sucessivamente, até
que o primeiro número (antes da vírgula), também chegue a 10."""

for i in range (1,11):
    print(f'({i},', end="")
    for j in range (1,11):
        print(f' {j}', end="")
    print(f')')