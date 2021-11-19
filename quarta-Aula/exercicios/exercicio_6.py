# Paracalcularamédiadobimestre,umprofessoratribuipesosdiferentesparacadaavaliação,deacordocomsuadificuldade.
# Elesempreaplica3avaliaçõesnobimestreeospesosvariamdebimestreparabimestre.Escrevaumprogramaquerealizeocálculoda
# médiadeumaluno.Oalgoritmodevereceberastrêsnotaseseus respectivos pesos, calcular e mostrar as médias das notas


primeira_prova = float(input("Digite a nota do primeira prova: "))
segunda_prova = float(input("Digite a nota do segunda prova: "))
terceira_prova = float(input("Digite a nota do terceira prova: "))

print("Digite o peso de cada prova, de 0 a 10")

primeira_peso = float(input("Digite o peso da primeira prova: "))
segunda_peso = float(input("Digite o peso da segunda prova: "))
terceira_peso = float(input("Digite o peso da terceira prova: "))

media = ((primeira_peso * primeira_prova) + (segunda_prova * segunda_peso) + (terceira_peso * terceira_prova)) / 10

print(f"O aluno tirou {primeira_prova} e o peso da prova era de : {primeira_peso}")
print(f"O aluno tirou {segunda_prova} e o peso da prova era de : {segunda_peso}")
print(f"O aluno tirou {terceira_prova} e o peso da prova era de : {terceira_peso}")

print(f"A media do Aluno foi de: {media}")


#ink utilizado paraentender sobre peso de provas:

#https://matematicabasica.net/media-ponderada/