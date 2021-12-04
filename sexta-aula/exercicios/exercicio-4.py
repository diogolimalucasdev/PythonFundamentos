"""
Escreva um programaque leia 20 números inteiros e a armazene em uma lista os numeros PARES e em outra lista
os números IMPARES. Ao final da leitura dos valores, imprima os valores das duas listas. Dica utilize o operador
% para verificar se um numero é par ou impar
"""


cont = 0
pares = []
impares = []

while cont <= 20:
    cont += 1
    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


# for i in pares:
#     print(f"Numeros pares: {i}")
print(f"Numeros pares: {pares}")
print(f"NUmeros impares { impares}")