# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

valor_hora = float(input('Quanto você ganha por hora? R$: '))
qtd_hora_mes = int(input('Quantas horas você trabalha no mês: '))
salario_bruto = qtd_hora_mes * valor_hora

inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
imposto_renda = (salario_bruto * 11) / 100

salario_liquido = (salario_bruto - imposto_renda) - sindicato - inss
print(f'Salário Bruto R$ {salario_bruto}')
print(f'Pagou ao INSS 8% do salario Bruto, pagando o valor de R$ {inss:.2f} reais')
print(f'Pagou ao SINDICATO 5% do salario Bruto, pagando o valor de R$ {sindicato:.2f} reais')
print(f'Pagou ao Imposto de Renda 11% do salario Bruto, pagando o valor de R$ {imposto_renda:.2f} reais')
print(f'Salário liquido a receber é de R$ {salario_liquido:.2f} reais')
