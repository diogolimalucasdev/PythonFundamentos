import modulos.interfaces as ui

"""
Modulo Contato reune as funções e  estrutura de dados necessarias para a manipulação e administração
dos contatos da agenda
"""

# Estrutura de dados que armazena os registros dos contatos

contatos_agenda = []


def criar_registro(nome, telefone, email):
    """
    Criar um dicionario contendo a estrutura do registro padrao do sistema e retorna uma
    copia com os valores
    """
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    return contato


def cadastrar_contato():
    ui.limpar_tela()
    print("======   Cadastrar novo Contato  ==========")
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    contato = criar_registro(nome, telefone, email)
    contatos_agenda.append(contato)


def listar_contato():
    contatos_agenda
    print("======   lista de contatos  ==========")
    print('{:^30} | {:^20} | {}'.format('Nome', 'Telefone', 'Email'))

    for contato in contatos_agenda:
        print('{:^30} | {:^20} | {}'.format(
            contato['nome'],
            contato['telefone'],
            contato['email']

            ))



def procurar_contato(nome):
    contatos_agenda

    for contato in contatos_agenda:
        if nome == contato['nome']:
            print('{:^30} | {:^20} | {}'.format('Nome', 'Telefone', 'Email'))
            print('{:^30} | {:^20} | {}'.format(
                contato['nome'],
                contato['telefone'],
                contato['email'] ))
            break

        else:
            print("Contato nao encontrado!")
            break
