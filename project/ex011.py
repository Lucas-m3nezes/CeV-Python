"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-lá, sabendo que 1l = 2m²"""

largura = float(input('Digite a altura da parede: '))
altura = float(input('Digite a largura da parede: '))

area = largura * altura
quantidadeTinta = area / 2


print('A área da parede é', area, 'metros quadrados.')
print('Você precisará de', quantidadeTinta, 'litros de tinta para pintar a parede.')
