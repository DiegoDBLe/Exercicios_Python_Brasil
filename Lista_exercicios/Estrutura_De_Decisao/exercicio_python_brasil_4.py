# 04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Informe uma letra: '))
vogal = ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print('A letra digitada é uma vogal!')
else:
    print('A letra digitada é uma consoante!')