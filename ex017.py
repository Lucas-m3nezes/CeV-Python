"""Faça um programa que leia um comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa."""


co = float(input('Comprimeito do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

from math import hypot
hipotenusa = hypot (co, ca)

print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
