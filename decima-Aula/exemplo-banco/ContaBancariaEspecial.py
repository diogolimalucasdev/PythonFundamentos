from ContaBancaria import ContaBancaria


# minha nova classe recebe todos os atributos da minha classe ContaBancaria
class ContaBancariaEspecial(ContaBancaria):

    # consigo adicionar atributos a minha nova classe utilizando os atributos da outra classe
    # igual no caso adiciono limite
    def __init__(self, nome="", cpf="", saldo=0.0, agencia="", numero="", limite=0.0):

        # utilizo a função super para acessar os metodos da minha classe pai
        # utilizo o super quando quero subescrever um metodo, eu utilizo o super
        super().__init__(nome, cpf, saldo, agencia, numero)


        # adiciono o limite
        self.limite = limite

    def sacar(self, valorSaque):
        if valorSaque <= self.saldo+ self.limite:
            self.saldo = self.saldo - valorSaque
            return valorSaque

        else:
            return 0


conta_especial = ContaBancariaEspecial("Diogo", "123.456.789-01", 500, "1234", "01234-8", 1000)
conta_especial.saldo = 200
print(f"Saldo inicial {conta_especial.saldo}")
print(f"Limite: {conta_especial.limite}")

conta_especial.sacar(950)
print(f"Saldo depois do saque: {conta_especial.saldo}")


conta2= ContaBancaria()

conta_especial.transferir(200, conta2)
print(f"Saldo da conta especial apos transferencia: {conta_especial.saldo}")
print(f"Saldo conta2: {conta2.saldo}")