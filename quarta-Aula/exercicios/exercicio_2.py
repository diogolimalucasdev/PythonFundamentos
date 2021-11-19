

#Escreva um programa que leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
# Aáreadocírculo é π *  raio2, considere π=3,141592

import math

raio = float(input("Digite o valor do raio do circuclo: "))
area_circulo = (raio ** 2) * math.pi
print(f"A area do ciruclo é {round(area_circulo,2)}")