# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e
# informe o tempo aproximado de download do arquivo usando este link (em minutos).
arquivo_MB = float(input('Informe o tamanho do arquivo em MB: '))
velocidade_net = float(input('Informe a velocidade do internet em Mbps: '))

# tempo = ((arquivo_MB * 8) / velocidade_net) / 60

tempo = arquivo_MB / velocidade_net
minuto = tempo * 60
print(f'Para baixar um arquivo de {arquivo_MB}MB vai demorar {minuto:.2f} minutos')

