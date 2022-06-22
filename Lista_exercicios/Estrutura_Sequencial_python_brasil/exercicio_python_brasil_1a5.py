# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print('Olá Mundo!')

# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = float(input('Informe um número: '))
print(f'O Numero informado foi {numero} ')

# 3 - Faça um Programa que peça dois números e imprima a soma.

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é {soma}')

# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1 = float(input('Informe a 1° nota do Bimestre: '))
nota_2 = float(input('Informe a 2° nota do Bimestre: '))
nota_3 = float(input('Informe a 3° nota do Bimestre: '))
nota_4 = float(input('Informe a 4° nota do Bimestre: '))

bimestre = [nota_1, nota_2, nota_3, nota_4]
soma = sum(bimestre)
media = soma / len(bimestre)

print(f'A média das notas do Bimestre foi: {media} ')

# 5 - Faça um Programa que converta metros para centímetros.
metros = float(input('Informe o valor da metragem m²: '))
centimetros = metros * 100
print(f'Convertendo o valor informado fica {centimetros} cm²')
