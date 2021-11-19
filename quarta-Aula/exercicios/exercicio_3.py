# Escreva um programa que leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
# em dólares

moeda_real = float(input("Digite um valore descubra a quanto vale em dólar: "))
dolar = 5.60

print(f"O valor R${moeda_real} corresponde a  {round(moeda_real / dolar,2)}$ em dólar")
