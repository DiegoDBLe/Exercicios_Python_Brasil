# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tamanho = float(input('Informe a metragem da area as ser pintada em m²: '))
rendimento = 3
tinta = tamanho / rendimento

lata = 18

preco_litro = 80.0 / lata
preco_gasto = preco_litro * tinta

print(f'Para a area de {tamanho:.2f}m², você vai precisar de {tinta:.2f} litro(s) de tinta e o total gasto será de R$ {preco_gasto:.2f} reais')