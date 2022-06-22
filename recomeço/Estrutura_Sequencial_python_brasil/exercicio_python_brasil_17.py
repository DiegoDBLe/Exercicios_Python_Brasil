# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
# de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.
tamanho = float(input('Informe a metragem da area as ser pintada em m²: '))
rendimento = 6
tinta = tamanho / rendimento

lata = 18
galoes = 3.6

rendimento_latas = tinta / lata
rendimento_galoes = tinta / galoes

sobra_latas = (rendimento_latas * lata) / tinta
sobra_galoes = (rendimento_galoes * galoes) / tinta

preco_litro_galao = 25 / galoes

preco_litro = 80.0 / lata
preco_gasto = preco_litro * tinta

preco_gasto_galoes = preco_litro_galao * tinta


# sobraL1 = (NLatas1 * lata1) - utilizacaoreal
# sobraL2 = (NLatas2 * lata2) - utilizacaoreal


print(f'18 Litros: Para a area de {tamanho:.2f}m², você vai precisar de {tinta:.2f} litro(s) de tinta e o total gasto será de R$ {preco_gasto:.2f}')
print(f'galões: Para a area de {tamanho:.2f}m², você vai precisar de {rendimento_galoes:.1f} galões de tintas e o total gasto será de R$ '
      f'{preco_gasto_galoes:.2f} reais')
print(f'Rendimento lata 18 litros: {rendimento_latas} vai sobrar {sobra_latas}')
print(f'Rendimento galão 3,6 litros: {rendimento_galoes} vai sobrar {sobra_galoes}')