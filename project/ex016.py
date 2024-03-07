"""Crie um programa que leia um número real pelo teclado e mostre a sua porção inteira"""


from math import trunc
valor = float(input('Digite um valor: '))

print(f'O valor digitado foi {valor} e a sua porção inteira é {trunc(valor)}')
