"""
erros em tempo de execução

"""
try:
    numero = int(input("Digite um numero: "))  # digite uma letra
    print(f"Numero digitado: {numero} ")

except:
    print("Voce nao digitou um numero inteiro!")
# como funciona....
""""
try:
    intruções

except NomeExcecao:
    instruções para tratamento de erro
"""

# tratamento de erro especifico
try:
    numero = int(input("Digite um numero: "))  # digite uma letra
    print(f"Numero digitado: {numero} ")

except ValueError as erro:
    print(f"Voce nao digitou um numero inteiro! Erro: {erro.args}")


# criando uma função para o tratamento de erro


def ler_inteiros(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor

        except:
            print("Valor invalido digite um valor inteiro!")


numero = ler_inteiros("Digite um numero: ")
print(numero)
