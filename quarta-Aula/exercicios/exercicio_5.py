# Escreva um programa que receba a altura e o raiode um cilindro circular e retorne o volume do cilindro.
# O volume de um cilindr ocircular é calculado por meio da seguinte fórmula:V = π * raio2* altura
import math
altura = float(input("Digite aaltura do cilindro: "))
raio = float(input("Digite o raio: "))

volume =math.pi * (raio ** 2) * altura

print(f"O valor do volume do cilindro é de: {round(volume,2)}")