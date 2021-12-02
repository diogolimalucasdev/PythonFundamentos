"""

Uma empresairáconcederumreajustedesalárioaosseuscolaboradoreselhecontrataramparadesenvolvero
programaquenomeeosaláriodeumcolaboradorecalculeoreajustesegundoo seguinte critério, baseado no salário atual:-

salários até R$ 1.100,00 (incluindo) : aumento de 20%
- salários entre R$ 1.100,00 e R$ 2.200,00 : aumento de 15%
- salários entre R$ 2.200,00 e R$ 3.500,00 : aumento de 10%
- salários de R$ 3.500,00 em diante : aumento de 5%Após o aumento ser realizado,
  informe na tela:
- o nome do funcionário- o salário antes do reajuste;- o percentual de aumento aplicado;- o valor do aumento;- o
novo salário, após o aumento.Paratestarseuprogramasoliciteosvaloresparaexecuçãodoalgoritmo(entradas/input).
Oalgoritmodeveráfuncionaratéumacondição de parada, definida por você seja atendida.

"""

while True:
    nome = input("Digite o nome do funcionario: ")
    salario = input(f"Digite o salario do {nome}: ")
    while not salario.isdigit():
        print("Digite apenas numero! ")
        salario = input(f"Digite o salario do {nome}: ")

    salario = float(salario)

    if salario <= 1100:
        aumento = 20 / 100
        valor_aumento = aumento * salario
        salario_final = salario + valor_aumento

        print(f"Nome do funcionario: {nome}")
        print(f"O salario antes do rajuste: {salario}R$")
        print(f"Percentual de aumento apicado:  {aumento * 100}%")
        print(f"Valor do aumento: {valor_aumento}R$")
        print(f"Valor do novo salario apos aumento {salario_final}R$")

    elif 1100 <= salario <= 2200:
        aumento = 15 / 100
        valor_aumento = aumento * salario
        salario_final = salario + valor_aumento

        print(f"Nome do funcionario: {nome}")
        print(f"O salario antes do rajuste: {salario}R$")
        print(f"Percentual de aumento apicado:  {aumento * 100}%")
        print(f"Valor do aumento: {valor_aumento}R$")
        print(f"Valor do novo salario apos aumento {salario_final}R$")

    elif 2200 <= salario <= 3500:
        aumento = 10 / 100
        valor_aumento = aumento * salario
        salario_final = salario + valor_aumento

        print(f"Nome do funcionario: {nome}")
        print(f"O salario antes do rajuste: {salario}R$")
        print(f"Percentual de aumento apicado:  {aumento * 100}%")
        print(f"Valor do aumento: {valor_aumento}R$")
        print(f"Valor do novo salario apos aumento {salario_final}R$")

    elif salario > 3500:
        aumento = 5 / 100
        valor_aumento = aumento * salario
        salario_final = salario + valor_aumento

        print(f"Nome do funcionario: {nome}")
        print(f"O salario antes do rajuste: {salario}R$")
        print(f"Percentual de aumento apicado:  {aumento * 100}%")
        print(f"Valor do aumento: {valor_aumento}R$")
        print(f"Valor do novo salario apos aumento {salario_final}R$")

    opcao = int(input("Digite [0] para sair do programa ou [1]para realizar outro aumento: "))

    if opcao == 0:
        print("Muito obrigado por usar o sistema, Digo Lima")
        break
    else:
        print("=================Novo procedimento=================")
