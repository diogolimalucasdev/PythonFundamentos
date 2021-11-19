# centralizando o texto ao centro ^
# O valor 50 siginifica quantas casas terão essa string

print("{:=^50}".format('Curso Python'))

# centralizando a esquerda <
print('{0:<30} |{1:.2f}'.format('Diogo', 8.5))

print(len("diogo"))



#dividir o nome pelo espaço ou outro caracter

nome = "diogo lima"
nome = nome.split(" ")
print(nome)
#pegandoo primeiro nome
print(nome[0])
#segundo nome,sobrenome
print(nome[1])


#Usando o replace para modifxar um caracter

modificar = "333.4646"
modificar = modificar.replace(".", ",")
print(modificar)


#pegando o nome quebrado, eu pego des do aparrtir ou seja aprtir do 0 e ate um antes 3

nome = "Diogo Lima"
print(nome[0:3])

#pegando apartir do 1 e ate 1 antes do 3
print(nome[1:3])