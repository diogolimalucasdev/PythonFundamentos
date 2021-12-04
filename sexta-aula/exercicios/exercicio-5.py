"""
Escreva um programa que leia a tmperatura média de cada mês do ano e armazene em uma lista.Apos isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês
elas correram (mostrar o mês por extenso 1-janeiro, 2-fevereiro...)
"""
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
       'novembro' ,'dezembro']
temperatura_mes = []

for i in range(len(mes)):
    temperatura = int(input(f"Digite a temperatura do mes de {mes[i]}: "))
    temperatura_mes.append(temperatura)

#
# print(temperatura_mes)
# print(len(temperatura_mes))
# print(len(mes))

# print(f"Tamanho da lista de temeperatura { len(temperatura_mes)}")
# print(f"Tamanho da lista de mes{len(mes)}")
media = round(sum(temperatura_mes) / len(mes), 2)

print(f"A media do ano foi de : {media}")
for i in range(len(mes)):
    if temperatura_mes[i] > media:
        print(f"A temperatura  do mes de {i+ 1} - {mes[i]}: ({temperatura_mes[i]}º)foi acima da media")

    else:
        pass