"""
Ponto de partidaq do sistema/programa(bootstrap)
"""
import modulos.interfaces as ui


"importo o interface  e apelido com UI"
import modulos.contatos as contatos

while True:
    opcao_escolhida = ui.exibir_menu()

    if opcao_escolhida == 1:
        print("Cadastrar um novo contato...")
        ui.aguardar(3)
        contatos.cadastrar_contato()


    elif opcao_escolhida == 2:
        print("Listar os Contatos...")
        ui.aguardar(3)
        contatos.listar_contato()


    elif opcao_escolhida == 3:
        print("Procurar um Contato...")
        ui.aguardar(3)
        nome = input('Digite o nome do contato: ')
        contatos.procurar_contato(nome)

    else:
        ui.aguardar(3)
        print("Obrigado por utilizar o Sistema, Diogo Lima Lucas")
        break
