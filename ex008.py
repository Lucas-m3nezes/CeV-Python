"""Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros."""


conversor = float(input('Digite quantos metros você deseja converter para centímetros e milímetros: '))
centimetros = conversor * 100
milimetros = conversor * 1000

print('{} metros convertidos para centímetros são: {}cm. Já para milímetros são: {}.'.format(conversor, centimetros, milimetros))