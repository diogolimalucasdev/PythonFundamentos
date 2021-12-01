"""
1)Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:- até 20 litros, 
desconto de 3% por litro- acima de 20 litros, desconto de 5% por litro
Gasolina:- acima de 20 litros, desconto de 4% por litro
Escreva um algoritmo que leia o número de litros vendidos,o tipo de combustível,
calcule e imprima o valor a ser pago pelo cliente,sabendo-se que o preço do litro da gasolinaé R$6,299,
e o preço do litro do álcool é R$ 5,199.
"""


print("1-Alcool\n 2-Gasolina")
tipo_combustivel = int(input("Digite o tipo do combustivel: "))
qtde = float(input("Digite quantos litros: "))


if tipo_combustivel == 1 and qtde <= 20:
    preco = qtde * 5.199 
    desconto = qtde * (3/100)
    preco_final =preco - desconto
    print(f"O preco total foi de: {round(preco, 2)} R$")
    print(f"Desconto de 3 % por litro == {round(desconto, 2)} %")
    print(f"Com desconto ficou {round(preco_final, 2)} R$")
    
elif tipo_combustivel == 1 and qtde > 20:
    preco = qtde * 5.199
    desconto = preco * (5/100)
    preco_final = preco - desconto
    print(f"O preco total foi de: {round(preco, 2)} R$")
    print(f"Desconto de 5 % por litro == {round(desconto , 2)} %")
    print(f"Com desconto ficou {round(preco_final, 2)} R$")
    
    
elif tipo_combustivel == 2 and qtde > 20:
    preco = qtde * 6.299
    desconto = qtde * (5/100) 
    preco_final = preco - desconto
    print(f"O preco total foi de: {round(preco, 2)} R$")
    print(f"Desconto de 5 % por litro == {round(desconto, 2) } %")
    print(f"Com desconto ficou {round(preco_final, 2)} R$")
    
else:
    preco = qtde * 6.299
    print(f"O valor foi de {round(preco)} R$ ")
    