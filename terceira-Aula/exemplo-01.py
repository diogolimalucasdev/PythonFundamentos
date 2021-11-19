"""
Objetivo:
Receber o valor de um determinado tipo de combustivele , a quantidade de litros abastecida.após receber
estes valores o algoritmo deve calcular o valor total abastecido e exbibir para o usuario
"""

# Entrada
# -Valor do combustivel
# -Qtde de litros

valor_combustivel = float(input("Valor do combustivel: "))

qtde_litros = float(input("Litros abastecidos: "))

# processamento
# -valor do combustivel * qtde de litros

total_abastecido = valor_combustivel * qtde_litros

# saida

# total abastecido
print(f"total Abastecido R${total_abastecido:2}")

#usando o format e decidindo que vou ter 5 casas decimais usando o d, ou seja tinha so duas e ele adicionou mais 3
#adicionando 3 zeros

print("total abastecido {:05d}".format(23))


#centralizando o texto

print("{:=^50}".format('Curso Python'))
