# importo tudo da minhaclasse exception
from exception import SaldoInsuficiente


##dados dentro da minha classe

# tipo de dado chamado ContaBancaria
class ContaBancaria:

    # def init é meu constructor, sempre sera executado quando a classe for chamada
    # self diz para o python que ele vai operar sobre o objeto que esta sendo construido
    def __init__(self, nome="", cpf="", saldo=0.0, agencia="", numero=""):
        self.nome_titular = nome
        self.cpf = cpf
        self.saldo = saldo
        self.agencia = agencia
        self.numero = numero

    def sacar(self, valorSaque):
        if valorSaque <= self.saldo:
            self.saldo = self.saldo - valorSaque
            return valorSaque
        else:
            raise SaldoInsuficiente("Saldo Insuficiente")

    def depositar(self, valorDepositado):
        if valorDepositado >= 0:
            self.saldo = self.saldo + valorDepositado
            return True
        else:
            return False

    def transferir(self, valorTransferir, contaDestino):
        if self.sacar(valorTransferir) > 0:
            # eu atribuo a conta destino o valor da transferencia
            return contaDestino.depositar(valorTransferir)

        else:
            False
