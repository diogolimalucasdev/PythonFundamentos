# Etiqueta - Elabore um programa que escreve na tela os dados de uma etiqueta,
# insira o nome completo do destinatário na primeira linha, o endereço na
# segunda, e o CEP, cidade e estado na terceira. (Dica: o site
# https://pt.fakenamegenerator.com/gen-random-br-br.php gerar nomes aleatórios. Utilize as
# informações geradas neste site em seus prints.)


nome = input("Digite seu Nome: ").upper()  # .upper() para deixar o nome em maiusculo
rua = input("Digite o nome da rua:  ").upper()
numero = input("Digite o numero da sua residencia: ")
cidade = input("Cidade: ").upper()
estado = input("Estado: ").upper()
cep = input("Cep: ")

print(nome)
print(rua + "," + numero )
print(cidade + "-" + estado)
print(cep)
