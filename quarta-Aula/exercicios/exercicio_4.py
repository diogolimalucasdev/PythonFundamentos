# Escreva um programa que leia um número entre 0 e 60 eimprimao seu sucessor,sabendo que o sucessor de 60é0.
# Não pode serutilizado nenhuma estrutura de seleção (decisão) e nem repetição.
numero = input("Digite um valor entre 0 e 60: ")

sucessor = int(numero) + 1

print(f"o sucessor de {numero} é {str(sucessor).replace('61', '0')}")
