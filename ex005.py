"""Faça um programa que leia um número inteiro  e mostre na tela o seu Antecessor e Sucessor."""


numero = int(input('Digite um número:'))
sucessor = numero + 1
antecessor = numero - 1

print('O sucessor do número {} é {}, já o seu antecessor é o número {}.'.format(numero, sucessor, antecessor))
