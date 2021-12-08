"""
escreva um programa que leia um numero indeterminado de valores, correspondente a notas, encerrando 
a enrada de dados quando for informado um valor igual a -1(que nao deve ser armazenado).Apos a entrada 
de dados faça:

a) mostre a quantidade de valores que foram lidos;
b) exiba todos os valores na ordem em que foram informados, um aqo lado do outro
c) Exiba todoss os valores na ordem inversa a que foram informados. um ao lado do outro
d) calcule e mostre a soma dos valores
e)calcule e mostre a média dos valores
f)calcule e mostre a quantidade de valoresacima da media calculada
g) calcule e mostre a quantidade de valores abaixo de sete
h)encerre o programa com uma mensagem

"""

notas = []

while True:
    nota = input("informe a nota: ").replace(",", ".")
    nota = float(nota)
    
    
    
    if nota == -1:
        break
    
    else:
        notas.append(nota)
        
        
print(f"Quantidade de notas informadas: {len(notas)}")

print("A notas em ordem em que foram informadas: ")
for i in notas:
    print(i, end=";")
    
    
notas.sort(reverse=True)
print("\nA notas em ordem inversa em que foram informadas: ")
for i in notas:
    print(i, end=";")
    
    
print(f"\nA soma de todas as notas {sum(notas)}")

media = round(sum(notas)/ len(notas), 2)

print(f"A media foi de: {media}")

acima_media = []

abaixo_media = []

for i in notas:
    if i > media:
        acima_media.append(i)
        
    else:
        pass
        
    if i < 7:
        abaixo_media.append(i)
        
        
print(f"Notas acima da media {len(acima_media)}")

print(f"Notas abaixo de sete:  {len(abaixo_media)}")

print("Onrigado por utilizar o sistema!")