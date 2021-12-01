# estou dizendo para o pytjon, estou criando uma estruturado tipo lista, uma lista vazia
nome_estrutura = []

# criando com valores, sempre separar por virgulas
# posições   0,       1,      2,       3
print("\n#criando com valores, sempre separar por virgulas#")
print("\nComando: nomes = ['Diogo', 'Maria', 'Miguel', 'Laryssa']")
nomes = ['Diogo', 'Maria', 'Miguel', 'Laryssa']

# acessando algum dos valores da lista, no caso o nome miguel
print("\n#acessando algum dos valores da lista, no caso o nome miguel#")
print("\nCOmando: nomes[2]")
print(nomes[2])

# utilizando numeros negativos, quando for numeros negativos o python inverte a sequencia
print("\n#utilizando numeros negativos, quando for numeros negativos o python inverte a sequencia#")
print("\nCOmando: print(nomes[-1])")
# exemplo
print(nomes[-1])

# verificando se um nome esta dentro da lista
print("\n#verificando se um nome esta dentro da lista#")
print("\nCOmando: 'Diogo' in nomes")
# ele retorna True para verdade e False para o contrario
print('Diogo' in nomes)

print("\nCOmando : 'Joao' in nomes")
print('Joao' in nomes)

# multiplicar a lista
print("\n#multiplicar a lista#")
print("\nCOmando : nomes2 *= 5")
nomes2 = ['Diogo', 'Maria', 'Miguel', 'Laryssa']
nomes2 *= 5
print(nomes2)

# contando quantas vezes o nome diogo aparece na lista
print("\n#contando quantas vezes o nome diogo aparece na lista#")
print("\nComando: nomes2.count('Diogo')")
print(nomes2.count('Diogo'))

# pegar eementos de uma lista e criar uma nova,começando na posição 1 a 3
print("\n#pegar eementos de uma lista e criar uma nova,começando na posição 1 a 3#")
print("\nComando: nomes3 = nomes[1:3]")
nomes3 = nomes[1:3]
print(nomes3)

# pegar elementos de uma lista e criar uma nova, começando em 0 e ate 4 pulando de 1 em 1
print("\n#pegar elementos de uma lista e criar uma nova, começando em 0 e ate 4 pulando de 1 em 1#")
print("\nComando: nomes4 = nomes[0:4:2]")
nomes4 = nomes[0:4:2]
print(nomes4)

# adicioando um novo elemento a a lista, ele adiciona apenas um elemento por vez
print("\n#adicioando um novo elemento a a lista, ele adiciona apenas um elemento por vez")
print("\nComando: nomes.append('novo_nome')")
nomes.append('novo_nome')
print(nomes)

# inserindo um elemento na posição determinando
print("\n# inserindo um elemento na posição determinando")
print("\ncomando: nomes.insert(0, 'novo_nome_primeiro')")
nomes.insert(0, 'novo_nome_primeiro')
print(nomes)

# remover o ultimo elemento, o pop  devolve o valor removido para algum lugar
print("\n#remover o ultimo elemento, o pop  devolve o valor removido para algum lugar")
print("\nComando: nome_removido = nomes.pop()")
print(f"Antes: {nomes}")
nome_removido = nomes.pop()
print(f"Nome removido: {nome_removido}")
print(f"Depois: {nomes}")

# remover um elemento especifico, eu preciso passar um elemento

print("\n#remover um elemento especifico, eu preciso passar um elemento")
print("\ncomando: nomes.remove('novo_nome_primeiro')")
print(f"Antes: {nomes}")
nomes.remove('novo_nome_primeiro')
print(f"Depois {nomes}")

# ordenando uma lista
print("\n#ordenando uma lista")

lista_numeros = [3, 5, 73, 2, 1, 32, 535, 68]
print(f"\nComando: lista_numeros.sort() ")
print(f"Antes: {lista_numeros}")
lista_numeros.sort()
print(f"Depois: {lista_numeros}")
