class MeutipoErro(Exception):
    pass


try:

    # o raise lança para meu computador um tipo de erro
    raise MeutipoErro

except MeutipoErro:
    print("Test")


    #No meu arquivo da aula 10, no banco crio um arquivo de Exception
