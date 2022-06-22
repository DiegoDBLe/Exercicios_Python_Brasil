import numpy

# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input('Informe o raio: '))
area = (raio ** 2) * numpy.pi
print(f'Area do circulo é: {area}')

# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

comprimento = float(input('Informe o Comprimento: '))
largura = float(input('Informe a Largura: '))
area = comprimento * largura
dobro = area * 2
print(f'Quadrado possui {area}m² e o dobro é {dobro}')

# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês.
valor_hora = float(input('Informe o valor da sua hora R$ '))
total_hora_mes = int(input('Informe quantas horas que você trabalha no mês: '))
salario = valor_hora * total_hora_mes
print(f'Esse mês seu salário é de R$ {salario:.2f}')

# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.  C = 5 * ((F-32) / 9).
temperatura_F = float(input('Informe a temperatura em F°: '))
celsius = (temperatura_F - 32) * (5/9)
print(f'Convertendo {temperatura_F:.2f}F° em celsius fica {celsius:.2f}C°graus ')

# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temperatura_C = float(input('Informe a temperatura em C°: '))
fahrenheit = (temperatura_C * 9/5) + 32
print(f'Convertendo {temperatura_C:.2f}C° em Fahrenheit fica {fahrenheit:.2f}F°')