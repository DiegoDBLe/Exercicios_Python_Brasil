# 08 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto_1 = float(input('Qual o preço do 1° produto(Mouse): R$ '))
produto_2 = float(input('Qual o preço do 2° produto(Teclado): R$ '))
produto_3 = float(input('Qual o preço do 3° produto(Cadeira Gamer): R$ '))

lista = {produto_1: 'Mouse', produto_2: 'Teclado', produto_3: 'Cadeira Gamer'}

print(f'O produto mais barato é: {min(lista.items())}')
