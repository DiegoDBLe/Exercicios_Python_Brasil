# 05 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input('Digita a 1° nota do aluno: '))
nota_2 = float(input('Digita a 2° nota do aluno: '))

media = (nota_1 + nota_2) / 2
if 7 <= media <= 9.9:
    print(f'Aprovado!\nMédia de {media}')
elif media < 7:
    print(f'Reprovado!\nMédia de {media}')
else:
    print(f'Aprovado com Distinção!\nMédia de {media}')
