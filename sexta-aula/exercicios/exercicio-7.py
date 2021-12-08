"""
Escreva um programa que preencha uma lista com modelos de 5 carros (Exemplos..hb20, gol...)
e em seguida o consumo deste carros, isto é quantos quilometros cada um deles faz com 1 litro de 
gasolina.Calcule e mostre.

a)O modelo mais enconomico
b) Quantos litros de gasolina cada um dos carros cadastrados consome para pecorrer uma distancia de 
1.000 km e quqanto isto custara, considerando que a gasolina custe R$ 6,299 o litro.


"""

from tabulate import tabulate


def cadastrar_carros(numero):
    carro = input("Digite o nome do carro: ")
    consumo = int(
        input("Informe quantos Km esse carrofaz com 1 litro de gasolina: "))
    carros = {
        "index": numero,
        "carro": carro,
        "consumo": consumo
    }
    return carros


modelos_cadastrados = []

modelos = 1
while modelos <= 3:
    modelos_cadastrados.append(cadastrar_carros(modelos))
    modelos += 1

# print(modelos_cadastrados)

menor = modelos_cadastrados[0]['consumo']
# print(menor)

for i in modelos_cadastrados:

    # mudei os nome aqui para nao dar conflito com a  minha tabela
    if i['consumo'] < menor:
        menor = i['consumo']
        nome = i['carro']
        numeracao = i['index']

listagem = []
for i in modelos_cadastrados:
    # crie essa variavel para usar a biblioteca  tabulate, onde ela ja formata uma tabela pra mim
    adicionar_tabela = i['index'], i['carro'], i['consumo'], i['consumo'] * 1000

    # aqui eu adiciono os itens a uma lista que vai me ajudar a formar a tabela
    listagem.append(adicionar_tabela)

    # print(f"\n Veiculo: {i['veiculo']}")
    # print(f"Nome: {i['carro']}")
    # print(f"Km por litro: {i['consumo']}")

# aqui eu utilizo a biblitoeca, onde o primeiro argumento é minha lista e o segundo é o titulo que eu quero para
# minha tabela
print(tabulate(listagem, headers=["Numeracao", "Modelo", "Consumo", "Em 1000KM"]))

print(f"O menor consumo é o do {nome}")
