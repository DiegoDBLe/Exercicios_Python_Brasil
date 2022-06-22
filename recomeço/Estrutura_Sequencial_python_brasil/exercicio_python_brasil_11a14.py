# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
n3 = float(input('Informe um número real: '))

produto = n1 * 2 * (n2 / 2)
print(f'O produto do dobro do primeiro com metade do segundo é : {produto}')

soma_triplo = (n1 * 3) + n3
print(f'A soma do triplo do primeiro com o terceiro é {soma_triplo}')

cubo = n3 ** 3
print(f'O terceiro elevado ao cubo é {cubo}')

# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Informe sua altura: '))
peso = (72.7 * altura) - 58
print(f'Seu peso ideal é de {peso:.2f}Kgs: ')

# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58 <-----> Para mulheres: (62.1*h) - 44.7
sexo = int(input('Informe seu sexo:\nFeminino[0]\nMasculino [1]'))
h = float(input('Informe sua altura: '))
if sexo == 0:
    peso_mulher = (62.1 * h) - 44.7
    print(f'Seu peso ideal é de {peso_mulher}Kgs.')
elif sexo == 1:
    peso_homen = (72.2 * h) - 58
    print(f'Seu peso ideal é de {peso_homen}Kgs.')
else:
    print(f'Escolha uma opção válida!')

# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso
# de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso_permitido = 50
multa = 4.0
peso_excedido = 0
peso_peixe = float(input('Informe o peso dos peixes Kgs: '))
if peso_peixe > peso_permitido:
    peso_excedido = peso_peixe - peso_permitido
    valor_multa = peso_excedido * multa
    print(f'Você excedeu o peso permitido de 50Kgs de peixe, passando {peso_excedido}kgs. Deverá pagar uma multa de R$ {valor_multa}')
else:
    print(f'Peso do peixe de acordo com o regulamento de pesca!')
