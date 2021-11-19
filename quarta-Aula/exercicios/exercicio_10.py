#Elabore um algoritmo que calcule o valor de uma prestação em atraso de um determinado bem.
# Considere a fórmula:prestacao<–valor + (valor * (taxa/100) * tempo)

valor = float(input("Digite o valor da prestação: "))
taxa = 0.02 # por dia
tempo = int(input("Digite o tempo em que esta em atraso: "))

prestacao = valor + (valor * taxa * tempo)

print(f"A taxa é de:  {taxa * valor * tempo}R$")
print(f"O valor final ficou: {prestacao}R$")

