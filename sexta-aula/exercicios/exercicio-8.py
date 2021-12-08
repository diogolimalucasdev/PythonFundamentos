"""
Uma empresa de transporte deseja realizar o calculo de km pecorrido em seusm itenarios.Para isto foi elaborada
planilha contendo a distancia entre as cidades.
"""
from tabulate import tabulate

cidades = [['Cidades', '', 'Sao Paulo', 'Campinas', 'Santos', 'Braganca Paulis', 'Socorro'],
           ["", "", 0, 1, 2, 3, 4],
           ['Sao Paulo', 0, 0, 98, 72, 90, 135],
           ['Campinas', 1, 98, 0, 170, 68, 110],
           ['Santos', 2, 72, 170, 0, 154, 210],
           ['Braganca Paulista', 3, 90, 68, 154, 0, 45],
           ['Socorro', 4, 135, 110, 210, 45, 0]

           ]

print(tabulate(cidades, tablefmt="fancy_grid"))

escolha = int(input("Digite o numero da cidadede origem: "))
#vou dentro da minha lista cidade e procuro o index
#Lembrando que o+2 é pra pular a linha da cidade e o do index da cidade
cidade_origem = cidades[escolha + 2]

##como estar partindo o km se inicia em 0
km_final = [0]

contagem = 0

while True:
    # print("Km andandos: ", km_final)

    # utilize um contador para saber se é o primeiro destino pois apartir dai eu consigo fazer a logicq
    if contagem == 0:

        # como é a primeira cidade ele escolheu a orgieeme agora escolhe o destino
        escolha_destino = int(input("Digite o codigo da cidade de Destino: "))
        if escolha_destino == -1:
            break

        # para descobrir a cidade eu entro dentro da lista de cidade
        # é o +2 é pra pular a linha cidades e a linha em branco
        cidade_destino = cidades[escolha_destino + 2]

        #para saber para aonde eu estou indo
        print(f"De {cidade_origem[0]} >>>>>>> {cidade_destino[0]}")

        # para acessar o km
        km_final.append(cidade_destino[escolha + 2])
    else:
        #print("entrou no primeiro else")

        #cidade origem é sempre a que ele escolheu por ultimo,entao como é umloop eu busco
        #o que ele escolheu na escolha destino
        cidade_origem = cidades[escolha_destino + 2]

        escolha_destino = int(input("Digite o codigo da nova cidade de Destino: "))
        if escolha_destino == -1:
            break
        else:
            #aqui eu so  apresento de onde ele ta siando e pra onde ele vai
            print(f"De {cidade_origem[0]} >>>>>>> {cidades[escolha_destino +  2][0]} ")

            #aqui eu vou dentro da linha da cidade de origem e o indice da cidade de destino
            # o +2 é pra pular o nome da cidade e o index dacidade
            km_final.append(cidade_origem[escolha_destino + 2])

    contagem = contagem + 1


#faço a somatoria de todos os valores
print(sum(km_final))
