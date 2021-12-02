"""
modulo contendo as funções que irão controlar as ações do usuario com as telas do sistema
"""
import os
import time


def limpar_tela():
    "verificar o sistema operacional"
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")


def aguardar(segundos):
    "Pausa a exibição da tela por uma quantidade de sgundos determinado utilizando abiblioteca TIME"
    time.sleep(segundos)


def exibir_menu():
    """
    Exibir ummenu com ações do sistemas. Ela aprestenta em texto o menu com um valor relacionado
    a ação que o usuario dseja executar no sistema.E retorna a opção escolhida pelo usuario
    """
    # limpar_tela() #No Pycharm nao funciona
    print("|============== Agenda de Contatos ===============| ")
    print("| 1    -   Cadastrar novo Contato                 |")
    print("| 2    -   Listar contatos cadastrados            |")
    print("| 3    -   Procurar um Contato                    |")
    print("| 4    -   Sair do Sistema                        |")
    print("|==============                      =============|")

    while True:
        opcao = int(input("Escolha uma opção: "))
        if 1 <= opcao <= 4:
            return opcao
        else:
            print("Opção Invalida,escolha uma opção que esteja no menu!")
