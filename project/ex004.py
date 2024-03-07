"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
sobre ela."""

start = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(start))
print('Só tem espaços?', start.isspace())
print('É um número?', start.isnumeric())
print('É alfabético?', start.isalpha())
print('É alfanumérico?', start.isalnum())
print('Está em maiúsculas?', start.isupper())
print('Está em minúsculas', start.islower())
print('Está capitalizada?', start.istitle())
