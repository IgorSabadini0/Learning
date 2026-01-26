precos = [30, 45, 50, 100, 200]
precosNovo = []

def desconto():
    global precos
    global precosNovo
    for preco in precos:
        if preco > 50:
            desconto = preco * 0.20
            precosNovo  = preco - desconto
            print(f"Preço {preco} com Desconto: {precosNovo}")
        else:
            print(f"Preço sem desconto: {preco}")

desconto()