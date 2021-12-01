# escreva um programa que calcule o total de um produto
# dados as seguinte listas


produtos = ['Banana', 'Maça', 'Tomate', 'Laranja']
qtdes = [5, 12, 28, 48]
precos = [2.5, 9.99, 6.45, 3.59]

total = 0
pos = 0

while pos < len(produtos):  # condição enquanto a posição for menor que o total de elementos
    subtotal = qtdes[pos] * precos[pos]
    total += subtotal
    print(f"{produtos[pos]}: R${subtotal}")

    pos += 1

else:
    print(f"Total de pedidos R$ {total}")




#Segunda maneira de se pecorrer


print("\n #Segunda maneira de se pecorrer")

total = 0

for indice, produto in enumerate(produtos):
    subtotal2 = qtdes[indice] * precos[indice]
    total += subtotal2
    print(f"{produto}: R$ {subtotal2}")
else:
    print(f"total de pedido R$: {total}")