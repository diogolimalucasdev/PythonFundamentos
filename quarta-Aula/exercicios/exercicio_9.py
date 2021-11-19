# Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldoa tual.
# Nesta instituição bancária é cobrado um valor para cada operação de retirada,o valor cobrado é de 0,38%
# sobreo valor retirado.Elabore um algoritmo que realize essas duasoperações e calcule o saldo final da conta
# ,considere que a conta possui saldo 0 (zero) no início do algoritmo.


valor_deposito = float(input('Digite o valor do deposito: '))

primeiro_cheque = float(input("Digite o valor do cheque: "))

segundo_cheque = float(input("Digite o valor do cheque: "))

saldo_final = valor_deposito - ((primeiro_cheque * 0.038) + (segundo_cheque * 0.038))


print(f"Taxa sobre o saquede {primeiro_cheque} foi de {primeiro_cheque * 0.038}R$")
print(f"Taxa sobre o saque de {segundo_cheque} foi de {segundo_cheque * 0.038}R$")
print(f"O saldo final da conta é de: {saldo_final}R$")