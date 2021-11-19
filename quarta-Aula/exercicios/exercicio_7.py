# Elabore um algoritmo que faça o cálculo de consumo médio de combustível de um carro apartir da distância
# percorrida(km) equantidade de combustível utilizada (litros)

km_pecorridos = int(input("Digite quantos Km foram pecorridos: "))
combustivel = int(input("Digite quantos litros: "))
consumo_medio = float(km_pecorridos/combustivel)
print(f"O comsumo medio foi de : {consumo_medio}Litros")
