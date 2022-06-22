# 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input('Informe o 1° número: '))
n2 = float(input('Informe o 2° número: '))
n3 = float(input('Informe o 3° número: '))

lista = [n1, n2, n3]

print(f'Ordem decrescente: {sorted(lista, reverse=True)}')
