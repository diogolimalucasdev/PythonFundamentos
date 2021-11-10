# 6) Empréstimo - Escreva um programa que exiba o valor total a ser pago em
# empréstimo bancário. O valor emprestado foi de R$ 10.000,00 e será pago em
# 12 prestações a juros mensais de 2,84%. Utilize a seguinte fórmula para calcular
# o valor total pago ao final do empréstimo:
# ValorFinal = ValorEmprestado * (1 + juros) ** meses


valor_emprestimo = 10000
juros_mes = valor_emprestimo * 0.0284
meses = 12
valor_total = (1 + juros_mes) * 12 + valor_emprestimo
valor_total2 = juros_mes * 12 + valor_emprestimo


print("O valor final a ser pago será de: ", valor_total)  # valor adicionando o 1 ao juros ao mes
print("O valor final a ser pago será de: ", valor_total2)  # valor sem adicionar o 1 ao juros ao mes
