# Elabore um algoritmo que calcule e apresente em metros por segundo o valor da velocidade de um projétil
# que percorre uma distância de quilômetros a um espaço de tempo em minutos.Utilize a fórmula
# velocidade = (distância * 1000) / (tempo* 60).

distancia = float(input("Digite a distancia pecorrida pelo projetil: "))
tempo = float(input("Digite o tempo gasto: "))

velocidade = round((distancia * 1000) / (tempo * 60),2)
km_hora= round(velocidade * 60,2)
metros_segundo = round(km_hora / 3.6,2)

print(f"{km_hora} Km/h em  {metros_segundo} m/s")
