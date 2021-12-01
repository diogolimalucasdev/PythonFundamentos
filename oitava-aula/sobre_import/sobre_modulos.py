#como fazer importação
#o pycache serve para compilar nossas bibliotea, assim agiliza nosso programa, toda vez que há uma modificação 
# ele atualiza essa compilação



#especificando o modulo que eu quero dentro do pacote
from random import randint, random

#utilizo o as para nao ter que escrever o nomo "inteiro"
import novotesteModulo as testenovo

#biblioteca do python
import datetime

#nossa 'biblioteca 
import testmodulo

testmodulo.somar()


#utilizando a improtação com o 'as'

testenovo.teste()




#utilizando a função rnadint e random que eu importei

print("aleatorio inteiro", randint(0, 10))
print("numero aleatorio float", random())