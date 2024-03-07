"""Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dolares ela pode comprar."""


saldo = float(input('Qual o seu saldo?: '))
converter = saldo / 3.27

print('Com R${} você pode comprar ${}.'.format(saldo, converter))
