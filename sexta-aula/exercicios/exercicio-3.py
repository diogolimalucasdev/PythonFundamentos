"""
Uma associação empresarial necessita de um programa para a realização e computação dos votos das 4 chapas inscritas.
Os codigos para computar os votos são:


111 - chapa 1
112 - chapa 2
113 - chapa 3
114 - chapa 4
999 - voto nulo
100 - voto em branco
(imprima a tabela acima a cada solicitação de voto)

Escreva um programa que calcule e mostre:
-O total de votos e percentual de votos válidos para cada (votos recebidos pela chapa, sobre o total de votos
excluindo os votos em branco e nulos) chapa

- o total de votos nulos
- Ototal d evotos em brancos
-A porcentagem de votos nulos sobre o total de votos
-A procentagem de votos em branco sobre o total de votos

Para finalizar o prorama considere a leitura do valor da senha 1234, quando realizada de um voto


"""

senha = 0
chapa1 = 0
chapa2 = 0
chapa3 = 0
chapa4 = 0
nulo = 0
branco = 0

print("Para encerrar a votação digite a mesma senha que abre a urna")
while senha != 1234:
    print("Urna aberta")
    cont = 0  # para calcular o total de votos
    while True:

        print("==== 111 - Chapa1      =======")
        print("==== 112 - Chapa2      =======")
        print("==== 113 - Chapa3      =======")
        print("==== 114 - Chapa4      =======")
        print("==== 999 - Voto Nulo   =======")
        print("==== 100 - Voto em Branco ====")

        voto = input("Digite seu voto: ")

        if voto == '1234':
            break
        else:
            cont += 1


        if voto == '111':
            chapa1 += 1

        elif voto == "112":
            chapa2 += 1

        elif voto == "113":
            chapa3 += 1

        elif voto == "114":
            chapa4 += 1

        elif voto == "999":
            nulo += 1


        elif voto == '100':
            branco += 1

        else:
            cont -= 1
            print("Voto incorredo!")

    senha = int(input("Digite a senha para acessar os resultados"))

    cont2 = 0
    while senha != 1234:
        cont2 += 1
        print("Senha incorreta!")
        senha = int(input("Digite a senha para acessar os resultados"))

        if cont2 == 5:

            """
            Se o usuario tentar acessar os resultados mas errar a senha 5 vzes o resultados dos votos serão zerados
            """

            print("Voce nao tem acesso aos resultados! ")
            nulo = 0
            chapa1 = 0
            chapa2 = 0
            chapa3 = 0
            chapa4 = 0
            branco = 0
            break


#calculando a porcentagem de cada


if chapa1 == 0:
    porc_chapa1 = 0
else:
    porc_chapa1 = chapa1/ cont

if chapa2 == 0:
    porc_chapa2 = 0
else:
    porc_chapa2 = cont / chapa2

if chapa3 == 0:
    porc_chapa3 = 0
else:
    porc_chapa3 = cont / chapa3


if chapa4 == 0:
    porc_chapa4 = 0
else:
    porc_chapa4 = cont / chapa4

if nulo == 0:
    porc_nulo = 0
else:
    porc_nulo = cont / nulo


if branco == 0:
    porc_branco = 0
else:

    porc_branco = cont/branco

print(f"Total de votos {cont}")
print(f"Total de votos da Chapa 1 foi de: {chapa1} que equivale a: {porc_chapa1 * 100} % ")
print(f"Total de votos da Chapa 2 foi de: {chapa2} que equivale a: {porc_chapa2 * 100}  %")
print(f"total de votos da Chapa 3 foi de: {chapa3} que equivale a: {porc_chapa3 * 100} %")
print(f"Total de votos da chapa 4 foi de: {chapa4} que equivale a: {porc_chapa4 * 100} %")
print(f"Total de votos Nulos foi de : {nulo} que equivale a: {porc_nulo * 100}  %")
print(f"Total de votos em Branco foi de : {branco} que equivale a: {porc_branco * 100}  %")


print("Finalizado a votação")


