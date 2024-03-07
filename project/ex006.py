"""Faça um algoritmo que leia um número e mostre seu doblo, triplo e sua raiz."""


numero = int(input('Digite um número:'))
dobro = numero * 2
triplo = numero * 3
raiz4 = numero ** (1/2)

print('O dobro do número {} é {}.'.format(numero, dobro))
print('O triplo do número {} é {}.'.format(numero, triplo))
print('A raiz quadrada do número {} é {}'.format(numero, raiz4))