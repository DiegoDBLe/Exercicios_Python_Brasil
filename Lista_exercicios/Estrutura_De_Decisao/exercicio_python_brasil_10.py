# 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
pergunta = str(input('Em que turno você estuda?\nM-matutino ou V-Vespertino ou N- Noturno: ')).upper().strip().split()

if pergunta == 'M':
    print('Bom Dia!')
elif pergunta == 'V':
    print('Boa Tarde!')
elif pergunta == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')