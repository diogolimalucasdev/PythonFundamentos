from ContaBancaria import ContaBancaria

# instanciando a classe e vendo o tipo dela
conta1 = ContaBancaria()
print(type(conta1))

# posso criar atributos, chamando a variavel que  representa a classe e defino a propriedade nome_titular
conta1.nome_titular = 'Diogo'
conta1.cpf = "123.456.789-20"
conta1.saldo = 1500.0
conta1.agencia = "1234-0"
conta1.numero = "01002345-0"

# depois de criar atributos eu posso acessar um atributo
print('nome:', conta1.nome_titular)
print('CPF:', conta1.cpf)
print('saldo:', conta1.saldo)
print('agencia:', conta1.agencia)
print('C/c:', conta1.numero)

# nao posso utilizar um atributo que eu criei em tempo de execução, por isso é importante declarar dentro da classe

conta2 = ContaBancaria()

conta2.nome = "Maria"
conta2.cpf = "123.456.789.40"

# isso causara um erro
print('nome:', conta2.nome_titular)
print('CPF:', conta2.cpf)
print('saldo:', conta2.saldo)
print('agencia:', conta2.agencia)
print('C/c:', conta2.numero)

print("COnta 3 =================")
conta3 = ContaBancaria("Diogo", "513.555.444.32", 100, "0333-1", "0200-1021")

print("operações de Teste")

# como acessar a função sacar dentro da minha classe no arquivo COntaBancaria
print(f"Valor que tem na conta : {conta1.saldo}R$")
print(f"Valor sacado { conta1.sacar(500)} R$")
print(f"Valor que sobrou: {conta1.saldo}")

valorDepositar = float(input("Valor aser depositado: "))
conta1.depositar(valorDepositar)
print(f"Novo Saldo : {conta1.saldo}R$")


print('Trnsferir da conta1 para conta2')
conta1.transferir(200, conta2)
print(f"Novo Saldo da conta 1 : {conta1.saldo}R$")
print(f"Novo Saldo da conta 2 : {conta2.saldo}R$")