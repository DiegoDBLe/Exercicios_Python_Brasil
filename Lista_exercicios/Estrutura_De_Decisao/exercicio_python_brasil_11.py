# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
# calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_atual = float(input('Informe o salário atual: R$ '))

vinte_porcento = (salario_atual / 100) * 20
quinze_porcento = (salario_atual / 100) * 15
dez_porcento = (salario_atual / 100) * 10
cinco_porcento = (salario_atual / 100) * 5

if salario_atual < 280:
    novo_salario = salario_atual + vinte_porcento
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado 20%\n'
          f'Valor do aumento: R$ {vinte_porcento:.2f}\n'
          f'Novo salário, após o aumento: R$ {novo_salario:.2f}')
elif 280 <= salario_atual < 700:
    novo_salario = salario_atual + quinze_porcento
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado 15%\n'
          f'Valor do aumento: R$ {quinze_porcento:.2f}\n'
          f'Novo salário, após o aumento: R$ {novo_salario:.2f}')
elif 700 <= salario_atual <= 1500:
    novo_salario = salario_atual + dez_porcento
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado 10%\n'
          f'Valor do aumento: R$ {dez_porcento:.2f}\n'
          f'Novo salário, após o aumento: R$ {novo_salario:.2f}')
else:
    novo_salario = salario_atual + cinco_porcento
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado 5%\n'
          f'Valor do aumento: R$ {cinco_porcento:.2f}\n'
          f'Novo salário, após o aumento: R$ {novo_salario:.2f}')
    


