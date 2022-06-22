# 07 - Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input('Informe o 1° número: '))
n2 = float(input('Informe o 2° número: '))
n3 = float(input('Informe o 3° número: '))

lista = [n1, n2, n3]

print(f'O menor número digitado foi: {min(lista)}')
print(f'O maior número digitado foi: {max(lista)}')