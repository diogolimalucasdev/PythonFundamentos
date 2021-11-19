#Faça um algoritmo que receba o número dehoras trabalhadas e o valordo salário mínimo.
# Calculeemostreosalárioareceberseguindo as regras abaixo:
# a)a hora trabalhada vale a metade do salário mínimo;
# b)osaláriobrutoequivaleaonúmerodehorastrabalhadasmultiplicado pelo valor da hora trabalhada;
# c)o imposto equivale a 3% do salário bruto;d)osalárioareceberequivaleaosaláriobrutomenosoimposto.

horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
salario_minimo = float(input("Digite o salario minino: "))


valor_horas= salario_minimo /horas_trabalhadas

salario_bruto = valor_horas * horas_trabalhadas

salario_liquido = salario_bruto - (salario_bruto * 0.03)

print(f"Valor das horas { valor_horas}")

print(f"Valor do salario bruto: {salario_bruto}")

print(f"o valor do desconto é de {salario_bruto * 0.03}")

print(f"Valor do salario liquido: {salario_liquido}")